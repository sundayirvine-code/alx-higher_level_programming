#!/usr/bin/python3
'''module: 4-inherits_from
'''
def inherits_from(obj, a_class):
    """ inherits_from: checks if an object is a subclass of given class
    Args:
        obj: object to check 
        a_class: class to check against
    Returns:
        True if object is a subclass otherwise false
    """
    return issubclass(type(obj), a_class)
