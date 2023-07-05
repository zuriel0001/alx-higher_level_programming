#!/usr/bin/python3
"""Define function that prints names"""


def say_my_name(first_name, last_name=""):
    """
    a function that prints My name is <first name> <last name>

    Args:
      first_name (str): The first name to print.
      last_name (str): The last name to print.

    Raises:
        TypeError: If either of first_name or last_name are not strings
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if not first_name:
        raise TypeError("say_my_name() missing 1 required positional "
                        "argument: 'first_name'")

    print("My name is {} {}".format(first_name, last_name))
