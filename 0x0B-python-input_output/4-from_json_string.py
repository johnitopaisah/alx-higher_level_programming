#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_obj):
    """Function that convert JSON file to string.
    
    Args:
        my_obj (str): The JSON file to be converted to string.
    Return:
        The string file
    """
    return json.loads(my_obj)
