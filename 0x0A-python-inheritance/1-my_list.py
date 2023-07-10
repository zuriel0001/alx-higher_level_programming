#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited list class MyList."""


class MyList(list):
    """printing for the built-in list class in sorted list."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
