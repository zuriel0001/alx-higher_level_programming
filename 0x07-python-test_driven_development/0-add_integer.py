#!/usr/bin/python3


def add_integer(a, b=98):
    """function that adds 2 integers"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    result = int(a) + int(b)  #  a and b must be first casted to integers if they are float
    return (result)
