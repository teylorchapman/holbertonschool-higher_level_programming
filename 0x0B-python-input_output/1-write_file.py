#!/usr/bin/python3
"""Writes a string to a text file (UTF8) and returns
the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to text file and returns the
    length of the string"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
