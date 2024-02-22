#!/usr/bin/python3
"""Defines a JSON file-reading function."""


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
