#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str) or roman_string is None):
        return (0)

    length = len(roman_string)
    rstr = roman_string
    total = 0
    nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    for i in range(length):
        if i + 1 < length and nums[rstr[i]] < nums[rstr[i + 1]]:
            total -= nums[rstr[i]]
        else:
            total += nums[rstr[i]]
        return total
    return (0)
