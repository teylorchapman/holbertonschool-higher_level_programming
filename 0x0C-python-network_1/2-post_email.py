#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter and displays the body
of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv

    uriel = argv[1]
    edmund = argv[2]

    dad = urllib.parse.urlencode({'email': edmund}).encode('utf-8')
    req = urllib.request.Request(uriel, dad)

    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')

        print(body)
