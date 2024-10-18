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

def find_shortest_combination(target, codes, max_length=4):
    """Find the shortest combination of codes that evaluates to the target ASCII number."""
    ascii_values = {}
    
    # Extract ASCII values from codes
    for code in codes:
        try:
            processed_code = process_code(code)
            ascii_value = eval(processed_code)
            ascii_values[code] = ascii_value
        except Exception:
            continue

    shortest_result = None
    shortest_length = float('inf')

    # Helper function to update shortest result
    def update_shortest(expression, original_code):
        nonlocal shortest_result, shortest_length
        current_length = len(original_code)
        if current_length < shortest_length:
            shortest_result = original_code
            shortest_length = current_length

    # Check individual codes first
    for code, value in ascii_values.items():
        if value == target:
            update_shortest(code, code)
            return shortest_result, shortest_length

    # Check combinations of codes
    for length in range(2, max_length + 1):
        for combo in combinations(ascii_values.items(), length):
            if sum(val for _, val in combo) == target:
                expression = "+".join(code for code, _ in combo)
                combined_code = f"chr({expression})"
                update_shortest(expression, combined_code)

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

# Main execution logic remains the same...


def find_combinations_in_range(n, codes):
    from itertools import combinations as iter_combinations
    from collections import defaultdict

    """Find combinations for all numbers from 0 to n."""
    ascii_values = {}
    value_to_codes = defaultdict(list)
    
    # Extract ASCII values from codes
    for code in codes:
        try:
            code = process_code(code)
            ascii_value = eval(code)
            ascii_values[code] = ascii_value
            value_to_codes[ascii_value].append(code)
        except Exception:
            continue

    # Precompute all possible sums up to n
    sums = defaultdict(list)
    for length in range(1, 4):  # Adjust the range based on your max_length
        for combo in iter_combinations(ascii_values.items(), length):
            total = sum(val for _, val in combo)
            if total <= n:
                sums[total].append("+".join(code for code, _ in combo))

    # Print results
    for number in range(n + 1):
        existing_code = min(value_to_codes[number], key=len) if number in value_to_codes else None
        combinations = sums[number]
        
        if combinations:
            shortest = min(combinations, key=len)
            if not existing_code or len(f"chr({shortest})") < len(f'chr({existing_code})'):
                print(f"{number},chr({shortest})")
            else:
                print(f"(Existing) {number}: chr({existing_code}) (Length: {len(f'chr({existing_code})')})")
        elif existing_code:
            print(f"(Existing) {number}: chr({existing_code}) (Length: {len(f'chr({existing_code})')})")
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
