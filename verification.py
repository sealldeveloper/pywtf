from io import StringIO
import pandas as pd
import sys
import re

def extract_csv_data(js_file):
    with open(js_file, 'r') as file:
        content = file.read()
        matches = re.finditer(r'(\w+)\s*=\s*`([\s\S]*?)`', content)
        return [(match.group(1), match.group(2).strip()) for match in matches]

def verify_python_code(variable_name, csv_data, python_version):
    df = pd.read_csv(StringIO(csv_data), header=None, names=['ASCIINUM', 'PYTHONCODE'])
    
    error_count = 0
    
    print(f"\n## Verifying {variable_name}")
    
    for _, row in df.iterrows():
        asciinum = row['ASCIINUM']
        python_code = row['PYTHONCODE']
        
        try:
            result = eval(f"ord({python_code})")
            if result != int(asciinum):
                if variable_name == 'newerPython' and python_version <= (3, 10):
                    print(f"Ignored mismatch for newerPython: ASCIINUM {asciinum}, Python code: {python_code}, Result: {result}")
                else:
                    print(f"Mismatch: ASCIINUM {asciinum}, Python code: {python_code}, Result: {result}")
                    error_count += 1
        except Exception as e:
            if variable_name == 'newerPython' and python_version <= (3, 10):
                print(f"Ignored error for newerPython: ASCIINUM {asciinum}, Python code: {python_code}")
                print(f"Error message: {str(e)}")
            else:
                print(f"Error evaluating: ASCIINUM {asciinum}, Python code: {python_code}")
                print(f"Error message: {str(e)}")
                error_count += 1

    return error_count

if __name__ == "__main__":
    js_file = 'pywtf.js'
    csv_data_list = extract_csv_data(js_file)
    
    # Get the Python version
    python_version = sys.version_info[:2]  # This gives a tuple like (3, 9) for Python 3.9
    
    if csv_data_list:
        total_error_count = 0
        for variable_name, csv_data in csv_data_list:
            error_count = verify_python_code(variable_name, csv_data, python_version)
            total_error_count += error_count
        
        if total_error_count > 0:
            print(f"\nVerification failed with a total of {total_error_count} error(s).")
            sys.exit(1)
        else:
            print("\nAll verifications passed successfully!")
    else:
        print("Failed to extract CSV data from the JavaScript file.")
        sys.exit(1)
