#!/usr/bin/python3
"""Define a Rectangle Class"""
class Rectangle:
    """ A Rectangle class with getter and setter methods"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """Returns rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            res = self.__height + self.__width
            return res * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        else:
            rect = ''
            for h in range(self.__height):
                rect += str(self.print_symbol) * self.width
                if h != self.__height -1:
                    rect += '\n'
            return rect

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        '''method: __del__i
           deletes instance of Rectangle class, and prints "bye" message
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
