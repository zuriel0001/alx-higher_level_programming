#!/usr/bin/python3
"""
This script
  - takes in a URL
  - sends a POST request to the passed URL
  - takes email as a parameter
  - displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}
    utf_params = urllib.parse.urlencode(params).encode('utf-8')
    req = urllib.request.Request(url, data=utf_params, method='POST')
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
