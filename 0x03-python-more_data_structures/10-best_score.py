#!/usr/bin/python3
def best_schore(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=lambda t: a_dictionary[t])
        
