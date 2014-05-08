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


# Defining the function that builds the database
def create_dictionary(filename, dirname, dictionary):
    filepath = os.path.join(dirname, filename)
    pipe = subprocess.Popen(["git", "log", "-1", "--format=%ad",
                              "--date=local", "--", filepath],
                              stdout=subprocess.PIPE)
    output, error = pipe.communicate()
    output = output[4:]
    if output != "":
        time = output.split(" ")[2]
        day = output.split(" ")[1].zfill(2)
        month = output.split(" ")[0]
        year = (output.split(" ")[3]).strip("\n")
        dictionary[dirname].append(
            [os.path.splitext(filename)[0],
            time, day, month, year])
    return dictionary


# Defining the function that generates the csv database
def create_csv(dictionary):
    f = csv.writer(open('up_to_date.csv', 'wb'))
    f.writerow(["Directory", "Language", "Time", "Day", "Month", "Year"])
    for directory, values in dictionary.items():
        for value in values:
            lang, time, day, month, year = value
            f.writerow([directory, lang, time, day, month, year])


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
                   dictionary = create_dictionary(filename, dirname, dictionary)
                except KeyboardInterrupt:
                    raise
    create_csv(dictionary)


# Calling main function
if __name__ == "__main__":
    main()
