import pandas as pd
import sys
import os

def read_csv_file(file_path):
    try:
        return pd.read_csv(file_path, header=None, names=['ASCIINUM', 'PYTHONCODE'])
    except Exception as e:
        print(f"Error reading CSV file {file_path}: {str(e)}")
        return None

def verify_python_code(variable_name, df, python_version):
    if df is None:
        return 0
    
    error_count = 0
    
    print(f"\n## Verifying {variable_name}")
    
    for _, row in df.iterrows():
        asciinum = row['ASCIINUM']
        python_code = row['PYTHONCODE']
        
        try:
            result = eval(f"ord({python_code})")
            if result != int(asciinum):
                if variable_name == 'newerPythonMappings' and python_version <= (3, 10):
                    print(f"Ignored mismatch for newerPythonMappings: ASCIINUM {asciinum}, Python code: {python_code}, Result: {result}")
                else:
                    print(f"Mismatch: ASCIINUM {asciinum}, Python code: {python_code}, Result: {result}")
                    error_count += 1
        except Exception as e:
            if variable_name == 'newerPythonMappings' and python_version <= (3, 10):
                print(f"Ignored error for newerPythonMappings: ASCIINUM {asciinum}, Python code: {python_code}")
                print(f"Error message: {str(e)}")
            else:
                print(f"Error evaluating: ASCIINUM {asciinum}, Python code: {python_code}")
                print(f"Error message: {str(e)}")
                error_count += 1

    return error_count

if __name__ == "__main__":
    csv_files = [
        ('originalMappings', 'data/originalMappings.csv'),
        ('periodMappings', 'data/periodMappings.csv'),
        ('astrixMappings', 'data/astrixMappings.csv'),
        ('newerPythonMappings', 'data/newerPythonMappings.csv')
    ]
    
    # Get the Python version
    python_version = sys.version_info[:2]  # This gives a tuple like (3, 9) for Python 3.9
    
    total_error_count = 0
    for variable_name, file_path in csv_files:
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} does not exist. Skipping.")
            continue
        
        df = read_csv_file(file_path)
        if df is not None:
            error_count = verify_python_code(variable_name, df, python_version)
            total_error_count += error_count
    
    if total_error_count > 0:
        print(f"\nVerification failed with a total of {total_error_count} error(s).")
        sys.exit(1)
    else:
        print("\nAll verifications passed successfully!")
