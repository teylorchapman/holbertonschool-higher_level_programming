#!/usr/bin/python3
"""a Square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """intializes Square subclass"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """returns a square description"""
        return("[Square] {}/{}".format(self.__size, self.__size))
