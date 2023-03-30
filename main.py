import argparse
import glob
import importlib.util
import os

# The Pattern for input and output files

INPUT_FILE_PATTERN = 'input/{}.in'
OUTPUT_FILE_PATTERN = 'output/{}.out'
LEVEL_PY_FILE = 'levels/lvl{}.py'




def init():
    """Create necessary folders if they don't exist"""
    for folder in ['input', 'output', 'levels']:
        if not os.path.exists(folder):
            os.mkdir(folder)


def main():
    """Run the main program"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--lvl', type=int, required=True)
    args = parser.parse_args()

    level_to_exec = args.lvl

    # Remove all files from the output folder (Clean up)
    for file_path in glob.glob('output/*'):
        os.remove(file_path)

    # Get the path to the level python file
    level_py_file = LEVEL_PY_FILE.format(level_to_exec)

    print('Reading from input file and parsing it to the level module')

    # Read the input file
    input_formatted = INPUT_FILE_PATTERN.format(f"level_{level_to_exec}")
    lvl_input = read_file(input_formatted)
        

    # Load the module from the file path
    spec = importlib.util.spec_from_file_location("lvl_module", level_py_file)
    lvl_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lvl_module)

    # Call the main() function within the imported module
    output = lvl_module.main(lvl_input)

    # Write the output to the output file
    output_formatted = OUTPUT_FILE_PATTERN.format(f"level_{level_to_exec}")
    save_file(output_formatted, output)
    
    

def read_file(file_name):
    """Read a file and return its contents"""
    if not os.path.exists(file_name):
        print(f'File {file_name} does not exist')
        return
    
    with open(file_name, 'r') as input_file:
        return input_file.read()
    
def save_file(file_name, content):
    """Save a file with the given content"""
    with open(file_name, 'w') as output_file:
        output_file.write(content)
        
        
        
if __name__ == '__main__':
    init()
    main()
