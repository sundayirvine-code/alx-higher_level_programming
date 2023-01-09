#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of, or if obj is an instance of a class that inherited from, the specified class.
    Return False otherwise.
    """
    return isinstance(obj, a_class)
