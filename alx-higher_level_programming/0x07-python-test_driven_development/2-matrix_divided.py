#!/usr/bin/python3
"""Module to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function to divide all elements of a matrix by a number
        Args:
            matrix (list of lists): The input matrix
            div (int or float): The number to divide by
        Returns:
            list of lists: A new matrix with elements divided by div
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
