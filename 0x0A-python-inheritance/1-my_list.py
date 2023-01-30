#!/usr/bin/python3
"""This is a class called MyList that inherits from list"""


class MyList(list):
    """Initalizing the class that inherits from list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
