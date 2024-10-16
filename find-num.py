import argparse
import csv
import itertools
import sys

def process_code(code):
    """Process the Python code segment."""
    if code.startswith('chr(') and code.endswith(')'):
        code = code[4:-1]
        if code == 'not()': return '(not())'
        return code
    else:
        return f"ord({code})"

def find_shortest_combination(target, codes, max_length=3):
    """Find the shortest combination of codes that evaluates to the target ASCII number."""
    ascii_values = {}
    
    # Extract ASCII values from codes
    for code in codes:
        try:
            code = process_code(code)
            ascii_value = eval(code)  # Assuming each code evaluates to its ASCII value
            if ascii_value <= 126 or len(code) < 35:
                ascii_values[code] = ascii_value
            # print(f"Code: {code}, ASCII Value: {ascii_value}")  # Debug print
        except Exception as e:
            print(f"Error evaluating code '{code}': {e}")  # Debug print
            continue

    shortest_result = None
    shortest_length = float('inf')

    # Check each code individually
    for code, value in ascii_values.items():
        if value == target:
            expression = code
            current_length = len(f"chr({expression})")
            if current_length < shortest_length:
                shortest_result = f"chr({expression})"
                shortest_length = current_length
            # print(f"Found single: {code} -> {value} = {target}")  # Debug print

    # Check pairs of codes
    for combo in itertools.combinations(ascii_values.items(), 2):  # Pairs
        (code1, val1), (code2, val2) = combo
        if val1 + val2 == target:
            expression = f"{code1}+{code2}"
            current_length = len(f"chr({expression})")
            if current_length < shortest_length:
                shortest_result = f"chr({expression})"
                shortest_length = current_length
            # print(f"Found pair: {code1}, {code2} -> {val1} + {val2} = {target}")  # Debug print

    # Check triplets of codes
    for combo in itertools.combinations(ascii_values.items(), 3):  # Triplets
        (code1, val1), (code2, val2), (code3, val3) = combo
        if val1 + val2 + val3 == target:
            expression = f"{code1}+{code2}+{code3}"
            current_length = len(f"chr({expression})")
            if current_length < shortest_length:
                shortest_result = f"chr({expression})"
                shortest_length = current_length
            # print(f"Found triplet: {code1}, {code2}, {code3} -> {val1} + {val2} + {val3} = {target}")  # Debug print
    
    # Check quads of codes
    for combo in itertools.combinations(ascii_values.items(), 4):  # Triplets
        (code1, val1), (code2, val2), (code3, val3), (code4, val4) = combo
        if val1 + val2 + val3 + val4 == target:
            expression = f"{code1}+{code2}+{code3}+{code4}"
            current_length = len(f"chr({expression})")
            if current_length < shortest_length:
                shortest_result = f"chr({expression})"
                shortest_length = current_length
            # print(f"Found quad: {code1}, {code2}, {code3}, {code4} -> {val1} + {val2} + {val3} + {val4} = {target}")  # Debug print

    # Return a tuple with two elements: result and length
    if shortest_result is not None:
        return shortest_result, shortest_length
    else:
        return None, None  # Ensure it returns two values


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
    """Find combinations for all numbers from 0 to n."""
    ascii_values = {}
    
    # Extract ASCII values from codes
    for code in codes:
        try:
            code = process_code(code)
            ascii_value = eval(code)  # Assuming each code evaluates to its ASCII value
            ascii_values[ascii_value] = code
            # print(f"Code: {code}, ASCII Value: {ascii_value}")  # Debug print
        except Exception as e:
            print(f"Error evaluating code '{code}': {e}")  # Debug print
            continue
    for number in range(0, n + 1):
        result, length = find_shortest_combination(number, codes)
        if result:
            if number in ascii_values.keys() and len(result) < len(ascii_values[number]):
                print(f"{number},{result}")
            if number not in ascii_values.keys():
                print(f"{number},{result}")
            else:
                print(f"(Existing) {number}: {result} (Length: {length})")
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
