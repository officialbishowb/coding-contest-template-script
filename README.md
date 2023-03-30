# Coding Contest Template Script

Template script for coding contest designed to be reused for each different level.

## Usage

1. Install the required packages by running

   ```bash
   pip install -r requirements.txt
   ```

   

2. Modify the variables `INPUT_FILE_PATTERN` and `OUTPUT_FILE_PATTERN` to match your desired input and output file patterns. 

2. Implement your logic to solve the level in `do_work`.

3. Save the modified code as `main.py`.

4. Put the files that have to be processed in the directory specified by the `INPUT_FILE_PATTERN` variable.

5. Run the script

   ```bash
   python main.py
   ```

## Configuration

The following variables can be modified to configure the script:

   - `INPUT_FILE_PATTERN`: This variable sets the filename pattern for the input files. By default, it is set to `'input/*.in'`, which matches all files with the `.in` extension in the `input/` directory. You can modify this variable to match a different filename pattern or directory structure.
   - `OUTPUT_FILE_PATTERN`: This variable sets the filename pattern for the output files. By default, it is set to `'output/*.out'`, which creates output files with the `.out` extension in the `output/` directory. You can modify this variable to change the filename pattern or output directory.

The following parts **MUST** be configured:

- `do_work`: This function processes the input and returns the result. You **have to**modify this function to implement your own processing logic.