#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    """function that deletes a key in a dictionary."""
    new_dictionary = a_dictionary.copy()
    if key and key in new_dictionary:
        del new_dictionary[key]

    return (new_dictionary)
