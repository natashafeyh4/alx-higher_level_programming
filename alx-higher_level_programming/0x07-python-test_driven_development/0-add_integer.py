#!/usr/bin/python3
"""Module to add two integers
"""

def add_integer(a, b=98):
    """Function to add two integers
        Args:
            a (int): First integer
            b (int, optional): Second integer, defaults to 98
        Returns:
            int: The addition of a and b
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)

# Test cases
if __name__ == "__main__":
    print(add_integer(1, 2))  # Should print 3
    print(add_integer(100, -2))  # Should print 98
    print(add_integer(2))  # Should print 100
    print(add_integer(100.3, -2))  # Should print 98
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)  # Should print 'a must be an integer or b must be an integer'
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)  # Should print 'a must be an integer or b must be an integer'
