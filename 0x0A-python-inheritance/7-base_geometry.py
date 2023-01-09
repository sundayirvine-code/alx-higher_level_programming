#!/usr/bin/python3
"""
This is a BaseGeometry class.
"""


class BaseGeometry:
    ''' Class: BaseGeometry
    '''
    def area(self):
        ''' area: raises an exception
        Args: none
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' integer_validator: validates value
        Args:
            name: a string
            value: an integer
        Raises: TypeError if value is not an iteger 
        and valueError if value is less than 0.
        '''
        if type(value) != int:
            raise TypeError('<name> must be an integer')
        if value < 0:
            raise ValueError('<name> must be greater than 0')
