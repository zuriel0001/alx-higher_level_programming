#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """return [[x**2 for x in row] for row in matrix] is another way"""
    return (list(map(lambda i: list(map(lambda num: num**2, i)), matrix)))

