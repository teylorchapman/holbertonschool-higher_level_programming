#!/usr/bin/python3
"""This is a module that validates `value`"""


class BaseGeometry:
    """makes an empty class"""
    pass

    def area(self):
        """raises the exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
