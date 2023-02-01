#!/usr/bin/python3
"""This class will be the `base` of all other classes
in this project. The goal of it is to manage `id`
attribute in all the future classes and to avoid
duplicating the same code"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initalizing"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
