#!/usr/bin/python3
"""Define the clasd Student"""


class Student:
    """Represent the class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialising objects of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if atrrs is None:
            return (self.__dict__)

        new_dict = {key: value for key, value in self.__dict__.items() if key in attrs}
        return (new_dict)
