#!/usr/bin/python3
"""This is a module for a function that returns True if the objext
is exactly an instance of the specified class, otherwise False"""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of a specific class"""
    return type(obj) == a_class
