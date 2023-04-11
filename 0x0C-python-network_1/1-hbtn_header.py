#!/usr/bin/python3
"""displays the value of the X-Request-Id"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    uriel = argv[1]

    with urllib.request.urlopen(uriel) as resp:
        head = resp.info()
        req_id = head['X-Request-Id']
        print(req_id)
