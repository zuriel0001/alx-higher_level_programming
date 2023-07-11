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
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return (self.__dict__)

        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {key: getattr(self, key) for key
                    in attrs if hasattr(self, key)}

        return self.__dict__

    def reload_from_json(self, json):
        """Method that replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
