#!/usr/bin/python3
""" Defines a class Sqaure"""
class Square:
    """ Square class definition"""
    def __init__(self, size = 0):
        """ Function to initialize the square.

        Args:
            size - the size of a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns the current square area"""
        return self.__size * self.__size
