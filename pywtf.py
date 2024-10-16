import sys
import csv
import argparse

def load_csv(filename):
    with open(f'data/{filename}.csv', 'r') as file:
        return {row[0]: row[1] for row in csv.reader(file) if len(row) == 2}

def map_characters(input_str, mappings):
    return '+'.join(mappings.get(str(ord(char)), f'<COULDNT FIND {ord(char)}>') for char in input_str)

def main():
    parser = argparse.ArgumentParser(description='Translate input using character mappings.')
    parser.add_argument('input', help='Input string or file path')
    parser.add_argument('-f', '--file', action='store_true', help='Treat input as a file path')
    parser.add_argument('-p', '--period', action='store_true', help='Use period mappings')
    parser.add_argument('-a', '--astrix', action='store_true', help='Use astrix mappings')
    parser.add_argument('-n', '--newer-python', action='store_true', help='Use newer Python mappings')
    parser.add_argument('-e', '--eval', action='store_true', help='Wrap output in exec()')
    args = parser.parse_args()

    # Load mappings
    original_mappings = load_csv('originalMappings')
    mappings = original_mappings.copy()

    if args.period:
        mappings.update(load_csv('periodMappings'))
    if args.astrix:
        mappings.update(load_csv('astrixMappings'))
    if args.newer_python:
        mappings.update(load_csv('newerPythonMappings'))

    # Get input
    if args.file:
        with open(args.input, 'r') as file:
            input_text = file.read()
    else:
        input_text = args.input

    # Process input
    output = map_characters(input_text, mappings)

    # Apply eval if requested
    if args.eval:
        output = f'exec({output})'

    print(output)

if __name__ == '__main__':
    main()
