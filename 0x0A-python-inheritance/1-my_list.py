#!/usr/bin/python3
"""Defines class MyList that inherited list"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    pass

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(list(self)))
