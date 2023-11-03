#!/usr/bin/python3
"""Module to print a square of #
"""


def print_square(size):
    """Function to print a square of #
    Args:
        size (int): The size length of the square
    Returns:
        None
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
