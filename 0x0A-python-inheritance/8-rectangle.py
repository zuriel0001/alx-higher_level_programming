#!/usr/bin/python3
"""DEfine Rectangle Module"""


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Initialitse rectangle parameters"""

        set.integer_validator("height", height)
        self.__height = height

        set.integer_validator("width", width)
        self.__width = width
