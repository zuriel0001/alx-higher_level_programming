#!/usr/bin/python3
"""Defines a function that write txt files"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to be written into
        text (str): The text to be written into the file.
    Returns:
        The number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
