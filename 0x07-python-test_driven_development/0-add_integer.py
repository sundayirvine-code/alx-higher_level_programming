#!/usr/bin/python3
"""a function that adds 2 integers."""
def add_integer(a, b=98):
    """Returns integer addition of a and b
    Args:
        a - first integer
        b - second integer

    Raises:
        TypeError if either a or b is a non integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
