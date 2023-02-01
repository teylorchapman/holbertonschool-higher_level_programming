#!/usr/bin/python3
"""Student class that defines a student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict representation of Student"""
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of Student Instance"""
        self.__dict__.update(json)
