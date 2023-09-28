#!/usr/bin/python3
"Model for peak finder"


def find_peak(list_of_integers):
    """
    Finds a peak in list_of_integers.

    Args:
        list_of_integers (list): A list of integers in which to find a peak.

    Returns:
        int or None: The peak element if found, or
        None if the list is empty or None.
    """

    integers_count = len(list_of_integers)

    if integers_count == 0:
        return None

    if integers_count == 1:
        return list_of_integers[0]

    if integers_count == 2:
        return max(list_of_integers)

    middle_index = int(integers_count / 2)
    peak = list_of_integers[middle_index]

    if peak > list_of_integers[middle_index - 1] and\
            peak > list_of_integers[middle_index + 1]:
        return peak
    elif peak < list_of_integers[middle_index - 1]:
        return find_peak(list_of_integers[:middle_index])
    else:
        return find_peak(list_of_integers[middle_index + 1:])
