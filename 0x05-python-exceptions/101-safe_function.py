#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """ a function that executes a function safely.
        Returns the result of the function,
        Otherwise, returns None if something happens during the function
    """
    try:
        output = fct(*args)
        return (output)

    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
