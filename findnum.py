import argparse
import csv
import sys
from collections import defaultdict
from itertools import combinations as iter_combinations


def test_expression(expr):
    """Test if an expression evaluates correctly and return its value."""
    try:
        result = eval(expr)
        return result
    except:
        return None

def find_shortest_combination(target, codes):
    """Find the shortest combination that produces chr(target)."""
    # Get numeric values from existing codes
    code_values = []
    for code in codes:
        if code.startswith('chr(') and code.endswith(')'):
            inner = code[4:-1]
            value = test_expression(inner)
            if value is not None and isinstance(value, int):
                code_values.append((inner, value))
    
    shortest = None
    shortest_len = float('inf')
    
    # Try combinations of the inner expressions (limit to 3 for performance)
    for combo_size in range(1, 4):  
        for combo in iter_combinations(code_values, combo_size):
            total = sum(val for _, val in combo)
            
            if total == target:
                # Direct combination
                if combo_size == 1:
                    expr = combo[0][0]
                else:
                    expr = '+'.join(f'({inner})' if '+' in inner or '-' in inner else inner 
                                  for inner, _ in combo)
                
                full_expr = f'chr({expr})'
                
                # Quick length check before expensive eval
                if len(full_expr) < shortest_len:
                    # Test if it actually works
                    if test_expression(full_expr) == chr(target):
                        shortest = full_expr
                        shortest_len = len(full_expr)
    
    return shortest, shortest_len if shortest else (None, 0)


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
    # Get original mappings
    original_mappings = {}
    for i, code in enumerate(codes):
        if i <= n:
            original_mappings[i] = code
    
    # Find shorter alternatives
    for number in range(n + 1):
        if number in original_mappings:
            original = original_mappings[number]
            shorter, shorter_len = find_shortest_combination(number, codes)
            
            if shorter and shorter_len < len(original):
                # Verify it actually works and produces the right character
                if test_expression(shorter) == chr(number):
                    print(f"{number},{shorter}")
                # If no shorter working combination found, don't print anything




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
        if result and test_expression(result) == chr(args.number):
            print(f"{args.number},{result}")
        else:
            print(f"{args.number}: No shorter combination found")

    # If a range of numbers is provided
    if args.range is not None:
        find_combinations_in_range(args.range, all_codes)

    # If a list of numbers is provided from a file
    if args.list is not None:
        with open(args.list, 'r') as list_file:
            numbers = [int(line.strip()) for line in list_file if line.strip().isdigit()]
        
        for number in numbers:
            result, length = find_shortest_combination(number, all_codes)
            if result and test_expression(result) == chr(number):
                print(f"{number},{result}")
            else:
                print(f"{number}: No shorter combination found")

if __name__ == "__main__":
    main()
