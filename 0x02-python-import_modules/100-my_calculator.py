#!/usr/bin/python3

if __name__ == "__main__":

    """perform basic arithmetics on cmd line"""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    opps = {"+": add, "-": sub, "*": mul, "/": div}
    if (sys.argv[2]) not in opps:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, sys.argv[2], b, opps[sys.argv[2]](a, b)))
