#!/usr/bin/python3
"""takes in a URL and an email address,
sends a ```POST``` request to the passed URL
with the email as a parameter, and finally
displays the body of the response"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    v = {'email': argv[2]}
    resp = requests.post(url, v)
    print(resp.text)
