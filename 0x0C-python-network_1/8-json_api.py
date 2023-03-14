#!/usr/bin/python3
"""takes in a letter and sends a ```POST```
request to ```https://0.0.0.0:5000/search_user```
with the letter as the parameter"""

import requests
import sys

if __name__ == "__main__":
    url = "https://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    resp = requests.post(url, data={'q': q})
    try:
        dict = resp.json()
        id = dict.get('id')
        name = dict.get('name')
        if len(dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception as c:
        print("Not a valid JSON")
