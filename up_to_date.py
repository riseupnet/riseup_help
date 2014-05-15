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

from collections import defaultdict
import csv
import tabulate

# Defining the function that builds the database
def create_dictionary(filename, dirname, dictionary):
    filepath = os.path.join(dirname, filename)
    pipe = subprocess.Popen(["git", "log", "-1", "--format=%at",
                              "--date=local", "--", filepath],
                              stdout=subprocess.PIPE)
    time, error = pipe.communicate()
    time = time.strip("\n")
    filename = os.path.splitext(filename)[0]
    if len(filename) == 2 and time != "":
        dictionary[dirname].append([filename, time])
    else:
        dictionary[dirname + "/" + filename.split(".")[0]].append(
            [filename.split(".")[1], time])
    return dictionary


# Defining the function that compares the timestamps of the files
#def compare(dirname, dictionary):
#    for directory, values in dictionary.items():
#        for value in values:
#            language, time = value
#            if language == "en":
#                time_en = time
#                for value in values:
#                    language, time = value
#                    if language != "en" and time < time_en:
#                         print(dirname, language)

# Defining main function
def main():
    args = docopt(__doc__, version="up_to_date XX")
    dictionary = defaultdict(list)
    for dirname, _, filenames in os.walk(
                                   args["<repository>"],
                                   topdown=False):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ".text":
                try:
                   dictionary = create_dictionary(
                                    filename, dirname, dictionary)
                except KeyboardInterrupt:
                    raise
    print(dictionary)
#        compare(dirname, dictionary)



# Calling main function
if __name__ == "__main__":
    main()
