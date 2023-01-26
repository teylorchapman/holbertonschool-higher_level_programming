#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """Function that prints a text with 2 new lines
    after each of these characters: . ? and :"""
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    for t in text:
        if t in ".?:":
            print(t, end="\n\n")
        else:
            print(t, end="")
