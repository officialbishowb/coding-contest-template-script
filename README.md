# Coding Contest Template Script

Template script for coding contest designed to be reused for each different level.

## Usage

1. Modify the variables `INPUT_FILE_PATTERN` and `OUTPUT_FILE_PATTERN` to match your desired input and output file patterns. 

2. Implement your logic to solve the level under levels/lvlX.py. The function `main(input:str)` is the entry point for the script. You **have to** add the function and modify the function to implement your own processing logic.

3. Put the files that have to be processed in the directory specified by the `INPUT_FILE_PATTERN` variable.

4. Run the script

   ```bash
   python main.py --lvl X
   ```

   where `X` is the level number. The script will process all files that match the `INPUT_FILE_PATTERN` variable and write the output to the files that match the `OUTPUT_FILE_PATTERN` variable.


## Configuration

The following variables can be modified to configure the script:

   - `INPUT_FILE_PATTERN`: This variable sets the filename pattern for the input files. By default, it is set to `'input/*.in'`, which matches all files with the `.in` extension in the `input/` directory. You can modify this variable to match a different filename pattern or directory structure.
   - `OUTPUT_FILE_PATTERN`: This variable sets the filename pattern for the output files. By default, it is set to `'output/*.out'`, which creates output files with the `.out` extension in the `output/` directory. You can modify this variable to change the filename pattern or output directory.

The following parts **MUST** be configured:

- 'levels/lvlX.py' - `def main(input:str)` function - This function is the entry point for the script. You **have to** add the function and modify the function to implement your own processing logic.