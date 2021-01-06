#!/usr/bin/env python3
"""
copy and change filename.
Copy file in current directory, append string to filename before extension
"""
import sys
import os
import shutil

usage_string = "cn.py <path> <str-to-append>"

def main():
    """ main function """
    if len(sys.argv) != 3:
        print(usage_string)
        sys.exit(-1)
    source_path = os.path.split(sys.argv[1])
    filename = source_path[1]
    name, extension = filename.split(".")
    new_filename = name + '_' + sys.argv[2] + "." + extension
    shutil.copy2(sys.argv[1], new_filename)


if __name__ == '__main__':
    main()
