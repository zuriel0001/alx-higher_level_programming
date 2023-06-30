#!/usr/bin/python3


def add_integer(a, b=98):
    """a function that adds 2 integers.
    a and b must be first casted to integers if they are float.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    return (result)
