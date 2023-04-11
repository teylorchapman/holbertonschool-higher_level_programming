#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    from urllib import request

    r = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(r) as p:
        p = p.read()

        print("Body response:")
        print("\t- type: {}".format(type(p)))
        print("\t- content: {}".format(p))
        print("\t- utf8 content: {}".format(p.decode('utf-8')))
