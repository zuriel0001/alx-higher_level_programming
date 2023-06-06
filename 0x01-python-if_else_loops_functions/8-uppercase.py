#!/usr/bin/python3

def uppercase(str):

    """a function to print string in uppercase."""
    for alphabet in str:
        if ord(alphabet) >= 97 and ord(alphabet) <= 122:
            alphabet = chr(ord(alphabet) - 32)
        print("{}".format(alphabet), end="")
    print("")
