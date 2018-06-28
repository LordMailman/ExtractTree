#!python
"""Python code to search through directories and find specific files"""

import os
import argparse
import warnings
from pyunpack import Archive, PatoolError
import ipdb

def extract(root, filename):
    """Extract the archive to it's containing folder"""
    try:
        Archive(os.path.join(root, filename)).extractall(root)
    except PatoolError as err:
        # warnings.warn(err.args)
        print('Failed to extract ' + os.path.join(root, filename))

# Define extractable extensions
VALID_EXT = ('.zip','.rar','.7z')

# import argparse to get target root dir
PARSER = argparse.ArgumentParser()
PARSER.add_argument('path',
                    help='Path to recursively extract from')
ARGS = PARSER.parse_args()

# Check path input
if os.path.isdir(ARGS.path) is not True:
    raise Exception('Path input to DirSearch must be a valid directory')

# Loop through all files
for root, directories, filenames in os.walk(ARGS.path):
    # ipdb.set_trace()
    for filename in filenames:
        if filename.endswith(VALID_EXT):
            print('Extracting ' + os.path.join(root, filename))
            extract(root, filename)

