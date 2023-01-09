#!/usr/bin/python3
"""a function that returns the list of attributes and methods of an object"""
def lookup(obj):
    """
    Args:
        obj: input object

    Return: list of attributes and methods
    """
    return dir(obj)
