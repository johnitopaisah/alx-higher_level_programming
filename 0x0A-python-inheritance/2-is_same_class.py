#!/usr/bin/python3
"""defines a class-checking function."""


def is_same_class(obj, a_class):
    """check if an object is exactly an instrance of a given class

    Args:
        obj (any): the object to check.
        a_class (type): The class to match the type of obj to.
    returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

