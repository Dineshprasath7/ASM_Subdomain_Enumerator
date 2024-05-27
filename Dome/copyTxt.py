import subprocess
import shutil
import os
import difflib

# Run the command
command = ["python", "Dome.py", "-m", "passive", "-d", "appviewx.com", "-o"]
subprocess.run(command)

# Define the source file and the destination directory
source_file = 'C:/Users/Localuser/Documents/REF/Dome/results/appviewx.com/subdomains.txt'  # replace with your file path
destination_dir = 'C:/Users/Localuser/Documents/REF/Dome/RER'  # replace with your directory

# Check if the file exists in the destination directory
base, extension = os.path.splitext(os.path.basename(source_file))
destination_file = os.path.join(destination_dir, f"{base}{1}{extension}")

i = 2
while os.path.exists(destination_file):
    destination_file = os.path.join(destination_dir, f"{base}{i}{extension}")
    i += 1

print("Copying file to RER folder ")
shutil.copy(source_file, destination_file)

print("Files in RER folder:")
files = os.listdir(destination_dir)
for i, file in enumerate(files, start=1):
    print(f"{i}. {file}")

# Select two files to compare
file1 = input("Enter the number of the first file to compare: ")
file2 = input("Enter the number of the second file to compare: ")

# Read the files
with open(os.path.join(destination_dir, files[int(file1)-1]), 'r') as f:
    text1 = f.readlines()
with open(os.path.join(destination_dir, files[int(file2)-1]), 'r') as f:
    text2 = f.readlines()


d = difflib.Differ()
diff = d.compare(text1, text2)
diff_list = list(diff)

# Print only the lines that are in one file but not in the other
for line in diff_list:
    if line.startswith('- ') or line.startswith('+ '):
        print(line)