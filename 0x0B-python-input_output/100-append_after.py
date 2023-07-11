#!/usr/bin/python3
"""Defines function that reads stdin line by line and computes metrics"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a new string after each occurrence of a search string in a file.

    Args:
        filename (str): The name or path of the file to modify.
        search_string (str): The string to search for in the file.
        new_string (str): The string to append after each occurrence of
                          the search string.

    Raises:
        FileNotFoundError: If the specified file is not found.

    """

    with open(filename, "r+") as file:
        original_lines = file.readlines()

        modified_lines = []
        for line in range(len(original_lines)):
            modified_lines.append(original_lines[line])

            if search_string in original_lines[line]:
                modified_lines.append(new_string)

        file.seek(0)
        file.write("".join(modified_lines))
