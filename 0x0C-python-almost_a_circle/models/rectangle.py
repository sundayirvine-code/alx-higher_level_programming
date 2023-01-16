#!/usr/bin/python3
'''
class Rectangle
'''
from models.base import Base

class Rectangle(Base):
    '''
    Rectangle: Defines a rectangle class
    Attr:
        __width: width
        __height: height
        __x: x
        __y: y
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width=width
        self.__height=height
        self.__x=x
        self.__y=y
