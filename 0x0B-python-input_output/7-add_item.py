#!/usr/bin/python3
"""adds all arguments to a Python list and
then saves them to a file"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    i = load_from_json_file("add_item.json")
except FileNotFoundError:
    i = []

for a in sys.argv[1:]:
    i.append(a)

save_to_json_file(i, "add_item.json")
