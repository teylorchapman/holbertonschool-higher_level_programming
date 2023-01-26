#!/usr/bin/python3
"""module to find the max integer in a list"""


def max_integer(list=[]):
    """function to find and return the max int in a list of ints
    if the list is empty, funtion returns None"""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
