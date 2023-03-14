#!/usr/bin/python3
"""script that fetches ```https://intranet.hbtn.io/status```"""
import requests

if __name__ == "__main__":
    resp = requests.get("https://intrannet.hbtn.io/status")
    json_cont = resp.jsons()

    print("Body response:")
    print("\t- type: {}".format(type(json_cont)))
    print("\t- content: {}".format(json_cont))
