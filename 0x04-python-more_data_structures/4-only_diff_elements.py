#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """ function that returns a set of all non common
    elements in two set compared"""
    non_common = (set_1 ^ set_2)
    return (non_common)
