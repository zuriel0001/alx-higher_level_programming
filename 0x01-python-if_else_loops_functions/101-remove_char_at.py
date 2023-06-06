#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(str, n):

    """replicate a string without the character at nth position"""
    if n < 0:
        return (str)
    new_str = (str[:n] + str[n+1:])
    return (new_str)
