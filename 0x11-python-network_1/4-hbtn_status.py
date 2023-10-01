#!/usr/bin/python3
"""
Script that fetches URL with requests package
"""
import requests


if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    t = res.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
