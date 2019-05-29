#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    names = []
    input_file = open(filename)
    input_text = input_file.read()
    input_file.close()

    # extract year from text
    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', input_text)
    if not year_match:
        sys.stderr.write('Year not found.\n')
        sys.exit(1)

    year = year_match.group(1)
    names.append(year)

    #extract names and ranks as tuples: (rank, boy_name, girl_name)
    ranks_tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', input_text)

    #split tuples and combine each name with its rank in dict
    rank_names = {}
    for rank, boy_name, girl_name in ranks_tuples:
        if boy_name not in rank_names:
            rank_names[boy_name] = rank
        if girl_name not in rank_names:
            rank_names[girl_name] = rank

    #take names and ranks from dict and add them to the results list
    sorted_names = sorted(rank_names.keys())
    for name in sorted_names:
        names.append(name + ' ' + rank_names[name])

    return names


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files

    # option flag
    create_summary = args.summaryfile

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for file in file_list:
        extract_names(file)


if __name__ == '__main__':
    main()
