#!/usr/bin/python3
"""Creating a function"""


def pascal_triangle(n):
    """
         function that returns a list of lists of integers
         representing the Pascal’s triangle of n
    """
    triangle = []
    if n <= 0:
        return []

    triangle.append([1])

    for i in range(1, n):
        row = [1]

        p_row = triangle[-1]

        for j in range(1, i):
            element = p_row[j - 1] + p_row[j]
            row.append(element)

        row.append(1)

        triangle.append(row)
    return triangle
