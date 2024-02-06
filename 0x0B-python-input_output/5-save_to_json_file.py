#!/usr/bin/python3
"""Defines function to writes json text to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes json to a file

    Args:
        my_obj (any) : object
        filename (str) : name of file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
