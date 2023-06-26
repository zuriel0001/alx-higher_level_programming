#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    el_count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            el_count += 1
        except IndexError:
            break

    print("")
    return (el_count)
