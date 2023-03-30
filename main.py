from time import sleep
import glob
import os
from alive_progress import alive_bar


# The pattern used to match input files.
# Used to find and iterate over all input files.
# Must be a valid glob pattern.
# See https://docs.python.org/3/library/glob.html
INPUT_FILE_PATTERN = 'input/*.in'

# The pattern used to match output files.
# Used to save the processed input to a file.
# Must contain a single asterisk ('*') which will be replaced by the input file name.
OUTPUT_FILE_PATTERN = 'output/*.out'

def do_work(input: str) -> str:
    """
    Processes the given input and returns the result.


    Parameters
    ----------
    input : str
        The input to process.
        
    Returns
    -------
    The processed result.
    """
    
    # your code here
    
    pass

files = glob.glob(INPUT_FILE_PATTERN)

# show a progress becaus it looks cool :)
with alive_bar(len(files)) as bar:
    # iterate over all input files
    for input_file in files:
        # read the input file
        with open(input_file, 'r') as f:
            input = f.read()
        
        # process the input
        output = do_work(input)
        
        # write the output to a file
        base = os.path.basename(input_file)
        filename, file_extension = os.path.splitext(base)
        
        output_file = OUTPUT_FILE_PATTERN.replace('*', filename)
        
        if(not os.path.exists(os.path.dirname(output_file))):
            os.makedirs(os.path.dirname(output_file))
            
        if os.path.exists(output_file):
            os.remove(output_file)
        
        with open(output_file, 'w') as f:
            f.write(output)
        
        # update the progress bar
        bar()
    