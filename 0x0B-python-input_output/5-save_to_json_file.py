#!/usr/bin/python3
"""writes an object to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file w JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
