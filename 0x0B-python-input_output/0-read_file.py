#!/usr/bin/python3
"""Defines function to read file"""


def read_file(filename=""):
    """reads a file

    Args:
        filename (str) : name of file
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
