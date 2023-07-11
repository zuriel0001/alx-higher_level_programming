#!/usr/bin/python3
"""Define function that Create object from a JSON file"""

import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""

    with open(filename) as file:
        return json.load(file)
