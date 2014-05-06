#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
up_to_date is a program that checks if the translations files are up to date with the English ones. It then builds a database and a textile file with this data.

Usage:
    up_to_date.py [--verbose]  <repository>
    up_to_date.py (-h | --help)
    up_to_date.py --version

Arguments:
    <repository>      The path to the repository containing the files

Options:
    -h  --help       Shows the help screen
    --version        Outputs version information
    --verbose        Runs the program as verbose mode
"""
import sys

try:
    from docopt import docopt  # Creating command-line interface
except ImportError:
    sys.stderr.write("""
        %s is not installed: this program won't run correctly.
        To install %s, run: aptitude install %s
        """ % ("python-docopt", "python-docopt", "python-docopt"))

import os
import subprocess

# Defining the function that builds the database
def database(filename, dirname):
    filepath = os.path.join(dirname, filename)
    if filename == "en.text":
        output = subprocess.call(["git", "log", "-1",
                                  "--format=%h|%ai", "--", filepath])
        print(filepath)
        print(output)


# Defining main function
def main():
    args = docopt(__doc__, version="up_to_date XX")
    for dirname, _, filenames in os.walk(
                                   args["<repository>"],
                                   topdown=False):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ".text":
                try:
                    database(filename, dirname)
                except KeyboardInterrupt:
                    raise


# Calling main function
if __name__ == "__main__":
    main()
