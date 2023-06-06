#!/usr/bin/python3

def uppercase(str):

    """a function to prints string in uppercase"""
    converted_char = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        converted_char += i
    print("{}".format(converted_char))
