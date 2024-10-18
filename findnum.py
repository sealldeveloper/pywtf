import argparse
import csv
from functools import lru_cache
import sys
from collections import defaultdict
from itertools import combinations as iter_combinations


@lru_cache(maxsize=None)
def process_code(code):
    """Process the Python code segment."""
    if code.startswith('chr(') and code.endswith(')'):
        code = code[4:-1]
        if code == 'not()': return '(not())'
        return code
    else:
        return f"ord({code})"

def wrap_max_range(number):
    """Wrap the number with max(range(<number>))"""
    return f"max(range({number}))"

def find_shortest_combination(target, codes, max_length=4):
    """Find the shortest combination of codes that evaluates to the target number."""
    ascii_values = {}
    
    print(f"\nSearching for combinations for target: {target}")
    
    # Extract values from codes
    for code in codes:
        try:
            value = eval(code)
            if isinstance(value, str) and len(value) == 1:
                ascii_values[code] = ord(value)
            elif isinstance(value, int):
                ascii_values[code] = value
        except Exception as e:
            print(f"Failed to evaluate code: {code}. Error: {str(e)}")
            continue

    shortest_result = None
    shortest_length = float('inf')

    # Helper function to update shortest result
    def update_shortest(expression):
        nonlocal shortest_result, shortest_length
        current_length = len(expression)
        
        if current_length < shortest_length or (current_length == shortest_length and expression < shortest_result):
            shortest_result = expression
            shortest_length = current_length
            print(f"Updated shortest: {shortest_result} (Length: {shortest_length})")

    # Check individual codes first
    print("\nChecking individual codes:")
    for code, value in ascii_values.items():
        if value == target:
            update_shortest(code)
            print(f"Exact match found: {code}")
            return code, len(code)  # Early return if exact match found

    # Sort codes by their ASCII values
    sorted_codes = sorted(ascii_values.items(), key=lambda x: x[1])

    # Check combinations of codes
    print("\nChecking combinations:")
    for length in range(2, max_length + 1):
        for combo in iter_combinations(sorted_codes, length):
            combo_sum = sum(val for _, val in combo)
            if combo_sum == target:
                expression = "+".join(process_code(code) for code, _ in combo)
                update_shortest(f'chr({expression})')
            elif combo_sum == target + 1:
                # If the combination sum is 1 more than the target, wrap it with max(range())
                expression = "+".join(process_code(code) for code, _ in combo)
                wrapped_expression = wrap_max_range(expression)
                update_shortest(f'chr({wrapped_expression})')
            elif combo_sum > target + 1:
                break  # Stop checking this length if sum exceeds target + 1

    if shortest_result is None:
        print(f"\nNo combination found for target {target}")
    else:
        print(f"\nShortest combination found: {shortest_result}")

    return shortest_result, shortest_length


def process_file(filename):
    """Process the CSV file and return a list of codes."""
    codes = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                codes.append(row[1])  # Assuming the second column contains the code snippets
    return codes


def find_combinations_in_range(n, codes):
    """Find combinations for all numbers from 0 to n."""
    ascii_values = {}
    value_to_codes = defaultdict(list)
    
    # Extract ASCII values from codes
    for code in codes:
        try:
            processed_code = process_code(code)
            ascii_value = eval(processed_code)
            ascii_values[processed_code] = ascii_value
            value_to_codes[ascii_value].append(code)
        except Exception:
            continue

    # Precompute all possible sums up to n + 1
    sums = defaultdict(list)
    for length in range(2, 4):  # Adjust the range based on your max_length
        for combo in iter_combinations(ascii_values.items(), length):
            total = sum(val for _, val in combo)
            if total <= n + 1:
                expression = "+".join(process_code(code) for code, _ in combo)
                sums[total].append(expression)

    # Find the shortest combination for each number
    results = {}
    for number in range(n + 1):
        existing_code = min(value_to_codes[number], key=len) if number in value_to_codes else None
        shortest = None
        shortest_length = float('inf')

        # Check existing code
        if existing_code:
            shortest = process_code(existing_code)
            shortest_length = len(existing_code)

        # Check direct combinations
        if number in sums:
            direct = min(sums[number], key=len)
            if len(f"chr({direct})") < shortest_length:
                shortest = direct
                shortest_length = len(f"chr({direct})")

        # Check combinations for number + 1
        if number + 1 in sums:
            wrapped = min(sums[number + 1], key=len)
            wrapped_expression = wrap_max_range(wrapped)
            if len(f"chr({wrapped_expression})") < shortest_length:
                shortest = wrapped_expression
                shortest_length = len(f"chr({wrapped_expression})")

        if shortest:
            results[number] = shortest

    # Print results
    for number in range(n + 1):
        if number in results:
            try:
                if len(f'chr({results[number]})') < len(value_to_codes[number][0]):
                    print(f"{number},chr({results[number]})")
            except:
                print(f"{number},chr({results[number]}) (NEW)")
        else:
            print(f"{number}: No combination found")




def main():
    parser = argparse.ArgumentParser(description="Process CSV files and find combinations.")
    
    # Default to data/originalMappings.csv
    parser.add_argument('files', nargs='*', default=['data/originalMappings.csv'], 
                        help='List of CSV files to process (default: data/originalMappings.csv)')
    
    # Optionally input a single number or a list of numbers from a file
    parser.add_argument('-n', '--number', type=int, help='Single number to find combination for')
    
    # New option to specify a range of numbers
    parser.add_argument('--range', type=int, help='Find combinations for numbers from 0 to n')
    
    parser.add_argument('-l', '--list', type=str, help='File containing a list of numbers to find combinations for')
    

    args = parser.parse_args()

    # Ensure at least one of number or list is provided
    if args.number is None and args.list is None and args.range is None:
        print("Error: You must provide either a single number (-n), a file with a list of numbers (-l), or use --check-inoptimal.")
        sys.exit(1)

    all_codes = []
    
    # Process specified files
    for filename in args.files:
        all_codes.extend(process_file(filename))

    # If a single number is provided
    if args.number is not None:
        result, length = find_shortest_combination(args.number, all_codes)
        if result:
            print(f"{args.number}: {result} (Length: {length})")
            try:
                evaluated_result = eval(result)
                print(f"Evaluation: {repr(evaluated_result)}")
            except Exception as e:
                print(f"Error during evaluation: {str(e)}")
        else:
            print(f"{args.number}: No combination found")

    # If a range of numbers is provided
    if args.range is not None:
        find_combinations_in_range(args.range, all_codes)

    # If a list of numbers is provided from a file
    if args.list is not None:
        with open(args.list, 'r') as list_file:
            numbers = [int(line.strip()) for line in list_file if line.strip().isdigit()]
        
        for number in numbers:
            result, length = find_shortest_combination(number, all_codes)
            if result:
                print(f"{number}: {result} (Length: {length})")
            else:
                print(f"{number}: No combination found")

if __name__ == "__main__":
    main()
