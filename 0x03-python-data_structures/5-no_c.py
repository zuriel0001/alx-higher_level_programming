#!/usr/bin/python3


def no_c(my_string):
    """print strig without c and C"""
    new_string = ""
    for i in my_string:
        if i != "c" and i != "C":
            new_string += i
    return (new_string)
