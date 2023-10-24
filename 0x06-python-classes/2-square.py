#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """Class to define a square."""
    
    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
