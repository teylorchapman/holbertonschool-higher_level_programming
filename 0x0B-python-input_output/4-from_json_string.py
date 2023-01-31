#!/usr/bin/python3
"""reeturns an object (Python Data Structure)
represented by a JSON string"""

import json


def from_json_string(my_str):
    """returns object (PDS) represented by a JSON string"""
    return json.loads(my_str)
