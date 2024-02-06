#!/usr/bin/python3
"""Defines function to reads json text from a file"""
import json


def load_from_json_file(filename):
    """reads json from a file

    Args:
        filename (str) : name of file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.loads(file.read())
