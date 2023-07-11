#!/usr/bin/python3
"""Defines funtion that produce Pascal's Triangle"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists which is the triangle.
    """

    if n <= 0:
        return []

    lines_in_triangle = [[1]]

    while len(lines_in_triangle) != n:
        tri = lines_in_triangle[-1]

        steps = [1]
        for i in range(len(tri) - 1):
            steps.append(tri[i] + tri[i + 1])
        steps.append(1)
        lines_in_triangle.append(steps)

    return lines_in_triangle
