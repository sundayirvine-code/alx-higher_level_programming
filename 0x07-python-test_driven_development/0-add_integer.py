#!/usr/bin/python3
"""a function that adds 2 integers."""
def add_integer(a, b=98):
    try:
        a = int(a)
    except:
        raise TypeError('a must be an integer')
    try:
        b = int(b)
    except:
        raise TypeError('b must be an integer')
    else:
        return a + b
