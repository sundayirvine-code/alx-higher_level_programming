#!/usr/bin/python3
''' Module: 2-is_same_class
'''

def is_same_class(obj, a_class):
    '''check if an object is an exact instace of given class
    Args:
        obj: The object to check
        a_class: The class to match the object type to
    Returns:
        True if obj is an instance of a_class
        Otherwise False
    '''
    return type(obj) == a_class
