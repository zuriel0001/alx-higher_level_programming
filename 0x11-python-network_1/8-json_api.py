#!/usr/bin/python3
"""A script that takes in a letter sends
   POST request to http://0.0.0.0:5000/search_user
   with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    leta = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": leta}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        jsonres = res.json()
        if jsonres == {}:
            print("No result")
        else:
            print("[{}] {}".format(jsonres.get("id"), jsonres.get("name")))
    except ValueError:
        print("Not a valid JSON")
