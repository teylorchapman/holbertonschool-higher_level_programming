#!/usr/bin/python3
"""print_square module"""


def print_square(size):
    """Function that will prints a square"""
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for t in range(size):
        for c in range(size):
            print("#", end="")
        print()
