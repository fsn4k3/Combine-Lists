# MADE BY FSNAKE

import os
import time
import sys

def combine_files_in_directory(output_file_path):
    # Get the directory of the script
    script_directory = os.path.dirname(__file__)

    combined_data = set()

    # Iterate through all files in the script's directory
    for filename in os.listdir(script_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(script_directory, filename)

            # Read data from the current file
            with open(file_path, 'r') as current_file:
                current_data = set(current_file.readlines())

            # Combine data and eliminate duplicates
            combined_data = combined_data.union(current_data)

    # Write the combined data to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(sorted(combined_data))

    # Animated loading bar
    print('\nProcessing files:')
    bar_length = 30
    for i in range(bar_length + 1):
        time.sleep(0.1)
        percent = i / bar_length
        sys.stdout.write('\r')
        sys.stdout.write("[%-30s] %d%%" % ('=' * int(bar_length * percent), percent * 100))
        sys.stdout.flush()

    # Celebratory completion message
    print('\n--------------------------------------------------------')
    print('|               Process Finished                       |')
    print('|------------------------------------------------------|')
    print(f'| Directory:   "{script_directory}"                   ')
    print(f'| Output File: "{output_file_path}"                   ')
    print('|                                                      |')
    print('|               All Files Combined!                    |')
    print('|                                                      |')
    print('--------------------------------------------------------')
# Example usage:
output_file_path = 'result.txt'

combine_files_in_directory(output_file_path)
