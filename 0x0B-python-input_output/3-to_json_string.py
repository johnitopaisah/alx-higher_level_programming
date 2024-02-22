#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Function that convert string to JSON file.
    
    Args:
        my_obj (str): The string to be converted to JSON.
    Return:
        The JSON file
    """
    return json.dumps(my_obj)
