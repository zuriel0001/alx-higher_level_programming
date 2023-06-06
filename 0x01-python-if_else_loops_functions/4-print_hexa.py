#!/usr/bin/python3
# 4-print_hexa.py

"""print numbers 0 to 98 in decimal and hexadecimal"""
for num in range(0, 99):
    num_in_hex = hex(num)

    print("{} = {}".format(num, num_in_hex))
