#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """Represent class Square"""

    def __init__(self, size=0):
        """Initialises the data"""
        self.size = size

    @property
    def size(self):
        """get/set the current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """initialise a new sqaure"""

        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ Returns current square area """
        return (self.__size ** 2)
