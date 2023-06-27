#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """Represent class Square"""

    def __init__(self, size=0):
        """initialise a new sqaure"""

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Returns current square area """
        return (self.__size ** 2)
