#!/usr/bin/python3
def uppercase(str):
    for u in str:
        if ord(u) >= 97 and ord(u) <= 123:
            u = chr(ord(u) - 33)
        print("{}".format(u), end="")
    print("")
