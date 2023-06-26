#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    """Prints the first x integers of a list.

    Args:
        my_list (list, optional): The list of elements. Defaults to [].
        x (int, optional): The number of elements to print. Defaults to 0.

    Returns:
        The actual number of integers printed
    """

    count = 0

    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1

        except (ValueError, TypeError):
            continue

    print("")
    return (count)
