#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
up_to_date is a program that checks if the translations files are up to date
with the English ones. It then builds a database and a textile file with
this data.

Usage:
    up_to_date.py [--verbose]  <repository>
    up_to_date.py (-h | --help)

Arguments:
    <repository>      The path to the repository containing the files

Options:
    -h  --help       Shows the help screen
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
    if len(filename) == 2 and time != "":            #To fix foo.en.text
        dictionary[dirname].append([filename, time])
    else:
        dictionary[dirname + "/" + filename.split(".")[0]].append(
            [filename.split(".")[1], time])
    return dictionary


# Defining the function that compares the timestamps of the files
def compare(dictionary, f):
    for directory, values in dictionary.items():
        for value in values:
            language, time = value
            if language == "en":
                time_en = time 
        for value in values:
            language, time = value
            if language.isalpha() == True and time < time_en:
                f.write("{:<60} {:<0} {:<0}".format(directory, language, "\n"))
      

# Defining main function
def main():
    args = docopt(__doc__)
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
    f = open("up_to_date.en.text", "w")
    f.write(
"""@title = "Up to date"

This page tracks down the help pages that have been translated, but are not up
to date with the original English page.

If a page is listed below, please don't use the translation and refer to the 
English page.



""")
    f.write("{:<60} {:<0} {:<0}".format("Page", "Language", "\n\n"))
    compare(dictionary, f)


# Calling main function
if __name__ == "__main__":
    main()
