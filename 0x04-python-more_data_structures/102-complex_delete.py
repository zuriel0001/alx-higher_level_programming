#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())

    for dictionary_val in key_list:
        if value == a_dictionary.get(dictionary_val):
            del a_dictionary[dictionary_val]

    return (a_dictionary)
