#!/usr/bin/python3
"""Defines function to appends text to a file"""


def append_write(filename="", text=""):
    """appends to a file

    Args:
        filename (str) : name of file
        text (str) : text to be written
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
