#!/usr/bin/python3
"""
   This script
    - fetches https://alx-intranet.hbtn.io/status.
    - uses urlib package
"""

import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as res:
        data = res.read()
        utf_data = data.decode('utf-8')
        resType = type(data)
        print(f"Body res:\n\t- type: {resType}\n\t\
- content: {data}\n\t- utf8 content: {utf_data}")
