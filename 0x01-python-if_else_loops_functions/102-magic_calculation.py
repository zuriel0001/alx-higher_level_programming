#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(a, b, c):

    """match bytecode given by alx"""
    if a < b:
        return (c)
    if c > b:
        return (a + b)

    calc = (a*b - c)
    return (calc)
