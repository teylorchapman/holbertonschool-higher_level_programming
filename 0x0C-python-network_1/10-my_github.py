#!/usr/bin/python3
"""takes your Github credentials (username and password)
and uses the GitHub API to display your ```id```"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    un = sys.argv[1]
    token = sys.argv[2]
    req = requests.get(url, auth=HTTPBasicAuth(un, token)).json()
    print(req.get('id'))
