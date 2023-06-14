#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_total = sum(tup[0] * tup[1] for tup in my_list)
    sum_den = sum(tup[1] for tup in my_list)

    return (sum_total / sum_den)
