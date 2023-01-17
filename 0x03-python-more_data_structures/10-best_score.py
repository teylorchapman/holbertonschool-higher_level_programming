#!/usr/bin/python3
def best_schore(a_dictionary):
    if a_dictionary:
        return max(a_dictionary, key=lambda t: a_dictionary[t])
