# ASM_Subdomain_Enumerator
This Python script is designed to automate the process of comparing domain data. It uses the 'Dome.py' script to gather domain data, stores the results, and then allows you to compare different sets of results.

## Features

- Domain Data Gathering: The script runs `Dome.py` in passive mode on a specified domain.
- Data Storage: The results are stored in a specified directory. If a file with the same name already exists, the script will automatically increment a number in the filename to avoid overwriting existing files.
- File Comparison: The script allows you to select two files from the results directory and compare them. Differences between the files are printed to the console.

## Usage

1. Run the script. It will automatically execute `Dome.py` on the specified domain and store the results.
2. The script will print a list of all files in the results directory. Enter the number of the first file you want to compare, then do the same for the second file.
3. The script will print the differences between the two files. Lines present in the first file but not the second will be prefixed with '- ', and lines present in the second file but not the first will be prefixed with '+ '.

## Dependencies

- Python 3
- 'Dome.py' script
- 'subprocess', 'shutil', 'os', 'difflib' Python libraries

## Note

Please ensure that the 'Dome.py' script is in the same directory as this script for it to function correctly.

## Credits
https://github.com/v4d1 for Dome tool
