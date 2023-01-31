#!/usr/bin/python3
"""reads a text file (UTF8) and prints to stdout"""


def read_file(filename=""):
    """reads the file and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
