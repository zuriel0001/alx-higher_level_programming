#!/usr/bin/python3
"""Define funtion that save json file"""
import json


def save_to_json_file(my_obj, filename):
    """ writes Object to a text file, using JSON representation"""

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
