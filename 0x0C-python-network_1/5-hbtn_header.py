#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the value of the variable
```X-Request-Id``` in the response header"""

if __name__ == "__main__":
    import requests
    from sys import argv
    print(requests.get(argv[1]).headers.get('X-Request-Id'))
