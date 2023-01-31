#!/usr/bin/python3
"""adds all arguments to a Python list and
then saves them to a file"""


from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    j = load_from_json_file("add_item.json")
except:
    j = []

save_to_json_file(j + argv[1:], "add_item.json")
