#!/usr/bin/python3

def uppercase(str):

    """a function to prints string in uppercase"""
    converted_char = ""
    for charr in str:
        if ord(charr) >= 97 and ord(charr) <= 122:
            charr = chr(ord(charr) - 32)
        converted_char += charr
    print("{}".format(converted_char))
