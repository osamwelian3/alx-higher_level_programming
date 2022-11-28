#!/usr/bin/python3
"""number_of_lines
"""


def number_of_lines(filename=""):
    """Takes in str filename to read the number of lines
    """

    with open(filename, encoding="utf-8") as f:
        no_lines = 0
        while True:
            line = f.readline()
            if not line:
                break
            no_lines += 1
        return no_lines
