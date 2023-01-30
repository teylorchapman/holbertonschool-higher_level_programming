#!/usr/bin/python3
"""This is a module that validates `value`"""


class BaseGeometry:
    """bg class"""
    def area(self):
        """raises the exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
