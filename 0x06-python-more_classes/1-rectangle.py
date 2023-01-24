#!/usr/bin/python3
"""this is a retangle class that defines a rectangle :)"""


class Rectangle:
    """rectangle class, holds height and width"""
    def __init__(self, width=0, height=0):
        """initializes the height and width of a rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width * self.__height) == 0:
            return
        return (self.__width + self.__height) * 2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
