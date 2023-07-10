#!/usr/bin/python3
"""DEfine Rectangle Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Initialitse rectangle parameters"""

        self.integer_validator("height", height)
        self.__height = height

        self.integer_validator("width", width)
        self.__width = width

    def area():
        """Represents Area of Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        str = "[" + str(self.__class__.__name__) + "] "
        str += str(self.__width) + "/" + str(self.__height)
        return (str)
