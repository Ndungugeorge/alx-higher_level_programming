#!/usr/bin/python3
"""Defines function that returns object from JSON representation"""
import json


def from_json_string(my_str):
    """json string to object

    Args:
        my_str (str) : json string
    Returns:
        Python data structure represented by my_str in json
    """
    return json.loads(my_str)
