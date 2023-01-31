#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8)
and returns then number of characters added"""


def append_write(filename="", text=""):
    """appends a string at the end of a file and
    returns the number of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
