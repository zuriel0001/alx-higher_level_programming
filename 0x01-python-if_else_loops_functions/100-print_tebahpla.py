#!/usr/bin/python3

""""Print alphabet in reverse order alternating upper- and lower-case."""

for ascii_number in range(122, 96, -1):
    if ascii_number % 2 == 1:
        ascii_number -= 32

    print("{:c}".format(ascii_number), end="")
