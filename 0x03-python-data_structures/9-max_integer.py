#!/usr/bin/python3


def max_integer(my_list=[]):
    """ return largest number in a list """

    largest = my_list[0]
    if len(my_list) == "":
        return (None)

    for i in range(len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]
    return (largest)
