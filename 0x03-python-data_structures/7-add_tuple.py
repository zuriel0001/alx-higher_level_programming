#!/usr/bin/python3

"""function that adds 2 tuples"""


def add_tuple(tuple_a=(), tuple_b=()):

    x_comp = ""
    y_comp = ""

    tuple_a += (0, 0)
    tuple_b += (0, 0)

    x_comp = tuple_a[0] + tuple_b[0]
    y_comp = tuple_a[1] + tuple_b[1]

    return (x_comp, y_comp)
