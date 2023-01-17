#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for t in range(len(my_list)):
        return [t if t != search else replace for t in my_list]
