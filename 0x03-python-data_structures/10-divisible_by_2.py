#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if len(my_list) == "":
        return

    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0 and my_list[i] >= 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return (multiples)
