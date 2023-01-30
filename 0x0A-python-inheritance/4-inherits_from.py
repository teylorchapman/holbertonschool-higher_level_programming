#!/usr/bin/python3
"""This is a module for a function that returns
True if the object is an instance of a class
that inherited (directly or indirectly) from
the specified class, otherwise False"""


def inherits_from(obj, a_class):
    """checks if obj is an instance of a class 
    or inherited from a class"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
