#!/usr/bin/python3
"""This is a module for a function that returns True if
the object is an instance of, or if the object is an instance
of a class that inherited from, the specified class, otherwise
False"""


def is_kind_of_class(obj, a_class):
    """Prints if the object is an instance of a class or a class
    it was inherited from"""
    print isinstance(obj, a_class)
