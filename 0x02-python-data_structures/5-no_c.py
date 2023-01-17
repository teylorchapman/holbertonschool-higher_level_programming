#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for t in my_string:
        if t != "c" and t != "C":
            new_string += t
        return new_string
