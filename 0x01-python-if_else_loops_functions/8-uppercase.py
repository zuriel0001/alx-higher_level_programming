#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):

    """function to print alphqbets in uppercase."""
    for alphabet in str:
        if ord(alphabet) >= 97 and ord(alphabet) <= 122:
            alphabet = chr(ord(alphabet) - 32)
        print("{}".format(alphabet), end="")
