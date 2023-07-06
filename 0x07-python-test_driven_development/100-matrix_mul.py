#!/usr/bin/python3
"""Defines a matrix multiplication function."""

def subtract(matrix1, matrix2):
    """
    Subtracts two matrices element-wise.
    """
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def add(matrix1, matrix2):
    """
    Adds two matrices element-wise.
    """
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def matrix_mul(m_a, m_b):
    """a function that multiplies two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if type(m_a) != list:
        raise TypeError("m_a must be a list")

    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


    if len(m_a) == 1:
        return [[m_a[0][0] * m_b[0][0]]]

    else:
        n = len(m_a)
        a11 = [[0 for j in range(n//2)] for i in range(n//2)]
        a12 = [[0 for j in range(n//2)] for i in range(n//2)]
        a21 = [[0 for j in range(n//2)] for i in range(n//2)]
        a22 = [[0 for j in range(n//2)] for i in range(n//2)]
        b11 = [[0 for j in range(n//2)] for i in range(n//2)]
        b12 = [[0 for j in range(n//2)] for i in range(n//2)]
        b21 = [[0 for j in range(n//2)] for i in range(n//2)]
        b22 = [[0 for j in range(n//2)] for i in range(n//2)]

        # Dividing matrices into 4 sub-matrices
        for i in range(0, n // 2):
            for j in range(0, n // 2):
                a11[i][j] = m_a[i][j]
                a12[i][j] = m_a[i][j + n // 2]
                a21[i][j] = m_a[i + n // 2][j]
                a22[i][j] = m_a[i + n // 2][j + n // 2]

                b11[i][j] = m_b[i][j]
                b12[i][j] = m_b[i][j + n // 2]
                b21[i][j] = m_b[i + n // 2][j]
                b22[i][j] = m_b[i + n // 2][j + n // 2]

        # Calculating p1 to p7
        p1 = matrix_mul(a11, subtract(b12, b22))
        p2 = matrix_mul(add(a11, a12), b22)
        p3 = matrix_mul(add(a21, a22), b11)
        p4 = matrix_mul(a22, subtract(b21, b11))
        p5 = matrix_mul(add(a11, a22), add(b11, b22))
        p6 = matrix_mul(subtract(a12, a22), add(b21, b22))
        p7 = matrix_mul(subtract(a11, a21), add(b11, b12))

        # Calculating c21, c21, c11 e c22
        c11 = subtract(add(add(p5, p4), p6), p2)
        c12 = add(p1, p2)
        c21 = add(p3, p4)
        c22 = subtract(subtract(add(p5, p1), p3), p7)

        # Joining sub-matrices into one matrix
        result_matrix = [[0 for j in range(n)] for i in range(n)]
        for i in range(0, n // 2):
            for j in range(0, n // 2):
                result_matrix[i][j] = c11[i][j]
                result_matrix[i][j + n // 2] = c12[i][j]
                result_matrix[i + n // 2][j] = c21[i][j]
                result_matrix[i + n // 2][j + n // 2] = c22[i][j]

    return (result_matrix)
