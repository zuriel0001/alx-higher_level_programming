#!/usr/bin/python3


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix
     Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        new matrix which is a division of the old matrix
    """
    if (type(matrix) != list or
            matrix == [] or
            not all(isinstance(row, list) for row in matrix) or

            not all((isinstance(ele, int) or isinstance(ele, float))
                    for row in matrix for ele in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # new_matrix = ([list(map(lambda ele: round(ele / div, 2), row))
    # for row in matrix])  # ---all in one line
    # another way to put it is below

    new_matrix = []
    for row in matrix:
        new_row = []
        for ele in row:
            new_row.append(round(ele / div, 2))

        new_matrix.append(new_row)

    return (new_matrix)
