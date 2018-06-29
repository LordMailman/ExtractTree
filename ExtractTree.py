#!python
"""Python code to search through directories and find specific files"""

import argparse
import os
from pyunpack import Archive, PatoolError
import time
import ipdb

# Get starting time
START_TIME = time.time()

def extract(root, filename):
    """Extract the archive to it's containing folder"""
    try:
        Archive(os.path.join(root, filename)).extractall(root)
    except PatoolError:
        print('Failed to extract ' + os.path.join(root, filename))

# Define extractable extensions
VALID_EXT = ('.zip','.rar','.7z')

# import argparse to get target root dir
PARSER = argparse.ArgumentParser()
PARSER.add_argument('path',
                    nargs='+',
                    help='Path to recursively extract from')
ARGS = PARSER.parse_args()

# Loop over every input path within KeyboardInterrupt try/catch
try:
    NUM_EXTRACTED = 0
    for path in ARGS.path:
        # Check path input
        if os.path.isdir(path) is not True:
            print('{} is not a valid directory.'.format(path))
            continue

        # Loop through all files
        for root, directories, filenames in os.walk(path):
            # ipdb.set_trace()
            for filename in filenames:
                if filename.endswith(VALID_EXT):
                    print('Extracting ' + os.path.join(root, filename))
                    extract(root, filename)
                    NUM_EXTRACTED += 1
except KeyboardInterrupt:
    print('Extraction Interrupted by KeyboardInterrupt (Ctrl+C)!')

# Print end time
TOTAL_TIME = time.time() - START_TIME
print('Extracted {0} files in {1} seconds'.format(NUM_EXTRACTED, TOTAL_TIME))
