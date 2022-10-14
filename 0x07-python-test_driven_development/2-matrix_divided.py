#!/usr/bin/python3
"""
File: 2-matrix_divided.py

By: Samson Tedla <samitedla23@gmail.com>

Defines a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix divided by div rounded to 2 decimal.

    Args:
        matrix (list): list of list of integers or floats
        div (int/float): the divisor
    Raises:
        TypeError: if matrix is not list of list of integers or floats
        TypeError: if each row of the matrix is not of the same size
        TypeError: if div is not a number (integer or float)
        ZeroDivisionError: if div is 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
                        raise TypeError("matrix must be a matrix (list of "
                                        "lists) of integers/floats")

    for k in range(len(matrix)):
        if len(matrix[k]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not (isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        row_list = []
        for j in range(len(matrix[i])):
            row_list.append(round((matrix[i][j] / div), 2))
        new_matrix.append(row_list)
    return new_matrix
