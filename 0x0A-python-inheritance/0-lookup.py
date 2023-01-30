#!/usr/bin/python3
"""This is a function that returns the list of available attributes and methods
of an object."""


def lookup(obj):
    """This method will return all properties and methods of the specified
    object, without the values"""
    return dir(obj)
