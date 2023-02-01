#!/usr/bin/python3
"""Student class that defines a student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (vars(self))
        newdict = {}
        for x in attrs:
            try:
                newdict[x] = vars(self)[x]
            except Exception:
                pass
            return newdict
