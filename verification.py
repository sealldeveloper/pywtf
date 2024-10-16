from io import StringIO
import pandas as pd
import sys
import re

def extract_csv_data(js_file):
    with open(js_file, 'r') as file:
        content = file.read()
        match = re.search(r'const\s+csvData\s*=\s*`([\s\S]*?)`', content)
        if match:
            return match.group(1).strip()
    return None

def verify_python_code(csv_data):
    df = pd.read_csv(StringIO(csv_data), header=None, names=['ASCIINUM', 'PYTHONCODE'])
    
    error_count = 0
    
    for _, row in df.iterrows():
        asciinum = row['ASCIINUM']
        python_code = row['PYTHONCODE']
        
        try:
            result = eval(f"ord({python_code})")
            if result != int(asciinum):
                print(f"Mismatch: ASCIINUM {asciinum}, Python code: {python_code}, Result: {result}")
                error_count += 1
        except Exception as e:
            print(f"Error evaluating: ASCIINUM {asciinum}, Python code: {python_code}")
            print(f"Error message: {str(e)}")
            error_count += 1

    if error_count > 0:
        print(f"\nVerification failed with {error_count} error(s).")
        sys.exit(1)
    else:
        print("\nAll verifications passed successfully!")

if __name__ == "__main__":
    js_file = 'pywtf.js'
    csv_data = extract_csv_data(js_file)
    
    if csv_data:
        verify_python_code(csv_data)
    else:
        print("Failed to extract CSV data from the JavaScript file.")
        sys.exit(1)