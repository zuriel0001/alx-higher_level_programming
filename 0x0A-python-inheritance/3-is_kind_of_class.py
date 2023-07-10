#!/usr/bin/python3
"""Module containing is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to be checked
        a_class (type): The class to match the type of obj with
    Returns:
        True if obj is an instance or inherited instance of a_class
        Otherwise - False.
    """

    if isinstance(obj, a_class):
        return (True)
    return (False)
