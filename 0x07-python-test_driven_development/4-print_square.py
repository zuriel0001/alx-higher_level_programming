#!/usr/bin/python3
"""Define function that prints squares in #"""


def print_square(size):
    """
       a function that prints a square with the character #

    Arg:
      size (int): The height/width of the square.

    Raise:
      TypeError: If size is not an integer.
      ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
