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
        if attrs is None:
            return (self.__dict__)

        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__
