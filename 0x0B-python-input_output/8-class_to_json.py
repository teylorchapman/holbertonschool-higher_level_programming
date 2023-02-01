#!/usr/bin/python3
"""returns the dictionary description with simple
data structre (list, dictionary, string, integer
and boolean) for JSON serialization of an object"""


def class_to_json(obj):
    """returns dictionary representation"""
    return obj.__dict__
