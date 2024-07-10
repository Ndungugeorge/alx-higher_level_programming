#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")

    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
