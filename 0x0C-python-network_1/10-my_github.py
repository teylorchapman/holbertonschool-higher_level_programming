#!/usr/bin/python3
"""takes your Github credentials (username and password)
and uses the GitHub API to display your ```id```"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    un = argv[1]
    token = argv[2]
    resp = requests.get(url, auth=HTTPBasicAuth(un, token)).json
    print(resp.get('id'))
