#!/usr/bin/python3


def max_integer(my_list=[]):
    """ return largest number in a list """
    largest = my_list[0]

    for i in range(len(my_list)):
        if len(my_list) == "":
            return (None)

        if my_list[0] < my_list[i]:
            largest = my_list[i]
    return (largest)
