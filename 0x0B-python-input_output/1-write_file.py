#!/usr/bin/python3
"""Defines function to writes text to a file"""


def write_file(filename="", text=""):
    """writes to a file

    Args:
        filename (str) : name of file
        text (str) : text to be written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
