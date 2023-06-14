#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        num_sq = lambda x: x**2
        new_matrix[i] = list(map(num_sq, matrix[i]))

    return (new_matrix)
