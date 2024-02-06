#!/usr/bin/python3
"""Defines function that returns JSON representation of a class"""


def class_to_json(obj):
    """object to json string

    Args:
        obj (any) : object
    Returns:
        JSON representation of my_obj as string
    """
    return obj.__dict__
