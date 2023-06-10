#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    """Prints a matrix of integers"""
    for row in matrix:
        for num in range(len(row)):   # iterate over elements in row
            if num == len(row) - 1:
                print("{:d}".format(row[num]), end="")
            else:
                print("{:d} ".format(row[num]), end="")
        print()
