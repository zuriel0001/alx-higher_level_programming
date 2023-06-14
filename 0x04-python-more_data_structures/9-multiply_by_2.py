#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    dir_2 = a_dictionary.copy()
    key_list = list(dir_2.keys())

    for i in key_list:
        dir_2[i] *= 2

    return (dir_2)
