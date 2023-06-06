#!/usr/bin/python3

"""print all small case alphabets without q and e"""

for alphabets in range(97, 123):
    if chr(alphabets) != 'q' and chr(alphabets) != 'e':
        print(f"{chr(alphabets)}", end="")
