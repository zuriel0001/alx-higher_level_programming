#!/usr/bin/python3
"""Defines class MyList that inherited list"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            super().__init__(args[0])
        else:
            super().__init__(args)

    def print_sorted(self):
        sorted_list = sorted(self, key=lambda x: (isinstance(x, int), x))
        print(sorted_list)
