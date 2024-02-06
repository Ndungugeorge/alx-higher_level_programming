#!/usr/bin/python3
"""Defines function that returns JSON representation of an object"""
import json


def to_json_string(my_obj):
    """object to json string

    Args:
        my_obj (any) : object
    Returns:
        JSON representation of my_obj as string
    """
    return json.dumps(my_obj)
