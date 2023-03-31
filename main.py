import argparse
import glob
import importlib.util
import os

# The Pattern for input and output files

INPUT_FILES_FOLDER = 'input/'
OUTPUT_FILES_FOLDER = 'output/{}'
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
    lvl_inputs = read_folder(INPUT_FILES_FOLDER)
        

    # Load the module from the file path
    spec = importlib.util.spec_from_file_location("lvl_module", level_py_file)
    lvl_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lvl_module)
    
    

    # Call the main() function within the imported module
    for file in lvl_inputs:
        file_content = read_file(file)
        output = lvl_module.main(file_content)
        
        # Write the output to the output file
        file_name = file.split('/')[-1] if '/' in file else file.split('\\')[-1]
        file_name = file_name.replace('.in', '.out')
        print(f'Writing to output file {file_name}')
        save_file(OUTPUT_FILES_FOLDER.format(file_name), output)
    
    

def read_folder(foldername):
    """Read a folder file and return the name of the files"""
    files = []
    
    # Read all files in the folder and save the name
    for file_path in glob.glob(f'{foldername}/*.in'):
        files.append(file_path)
        
    return files
    
def read_file(file_name):
    """Read a file and return the content"""
    with open(file_name, 'r') as input_file:
        return input_file.read()
    
    
def save_file(file_name, content):
    """Save a file with the given content"""
    with open(file_name, 'w') as output_file:
        output_file.write(content)
        
        
        
if __name__ == '__main__':
    init()
    main()
