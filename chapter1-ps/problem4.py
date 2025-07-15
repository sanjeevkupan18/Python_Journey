import os

def print_directory_contents(directory):
    # List all files and directories in the given directory
    contents = os.listdir(directory)
    
    # Print each item in the directory
    for item in contents:
        print(item)

# Replace 'path_to_your_directory' with the path to the directory you want to inspect
directory_path = 'path_to_your_directory'

print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)
