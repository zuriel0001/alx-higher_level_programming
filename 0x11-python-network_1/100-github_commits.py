#!/usr/bin/python3
"""
Script to lists the
     10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    res = requests.get(url)
    commits = res.json()
    try:
        for num in range(10):
            print("{}: {}".format(
                commits[num].get("sha"),
                commits[num].get("commit").get("author").get("name")))

    except IndexError:
        pass
