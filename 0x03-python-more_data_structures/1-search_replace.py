#!/usr/bin/python3
def search_replace(my_list, search, replace):
     new = [ ]
     for e in range(len(my_list)):
         return [e if e != search else replace for e in my_list]
