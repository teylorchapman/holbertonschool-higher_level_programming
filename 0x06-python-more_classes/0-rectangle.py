#!/usr/bin/python3
"""this is a retangle class that defines a rectangle :)"""


class Rectangle:
        """Rectangle Class, holds height and width"""
        def __init__(self, width=0, height=0):
                """initializes the height and width of the rectangle"""
                if type(width) is not int:
                        raise TypeError("width must be an integer")
                if type(width) < 0:
                        raise ValueError("width must be >= 0")
                if type(height) is not int:
                        raise TypeError("height must be an integer")
                if type(height) < 0:
                        raise ValueError("height must be >= 0")

                self.width = width
                self.height = height
                
                @property
                def size(value):
                        return(self.__width)
        
                @width.setter
                def width(self, value):
                        if type(value) is not int:
                                raise TypeError("width must be an integer")
                        if value < 0:
                                raise ValueError("width must be >= 0")
                        self.__width = value
            
                @property
                def height(value):
                        return self.__height
        
                @height.setter
                def height(self, value):
                        if type(value) is not int:
                                raise TypeError("height must be an integer")
                        if type(value) < 0:
                                raise ValueError("height must be >= 0")
                        self.__height = value
