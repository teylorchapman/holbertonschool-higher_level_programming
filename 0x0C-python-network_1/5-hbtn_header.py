#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the value of the variable
```X-Request-Id``` in the response header"""

if __name__ == "__main__":
    import requests
    from sys import stderr

    url = input("Enter URL: ")

    resp = requests.get(url)

    if resp.status_code == 200:
        print(resp.headers['Z-Request-Id'])
    else:
        print("Request failed with status code", resp.status_code,
              file=stderr)
