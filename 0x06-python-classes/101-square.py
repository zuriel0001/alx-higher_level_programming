#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """Represent class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialises the data"""
        self.size = size
        self.position = position

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

    def my_print(self):
        """print the square in the '#' characters"""
        if (self.__size == 0):
            print("")

        else:
            for i in range(self.__position[1]):
                print("")

            for j in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")

                for z in range(self.__size):
                    print("#", end="")

                print("")

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """  """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value


    def __str__(self):
        """Define the print() representation of a Square."""

        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]

            if i != self.__size - 1:
                print("")

        return ("")

