#!/usr/bin/python3
"""Defines a txt file-reading function."""


def read_file(filename=""):
    """Print the content of a UTF8 file to  stdout.

    Args:
        filename (str): The name of the file to read.
    Returns:
        The number of characters written.
    """
    with open(filename, encoding= "utf-8") as f:
        print(f.read(), end="")
