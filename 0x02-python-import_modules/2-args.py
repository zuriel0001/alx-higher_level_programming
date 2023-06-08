#!/usr/bin/python3
if __name__ == "__main__":

    """print the number of arguments and list of them"""

    import sys

    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print("0 arguments.")

    elif arg_count == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(arg_count))

    for arg_count in range(arg_count):
        print("{}: {}".format(arg_count + 1, sys.argv[arg_count + 1]))
