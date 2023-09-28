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

    loi = list_of_integers
    if loi == []:
        return None
    total = len(loi)
    if total == 1:
        return loi[0]
    elif total == 2:
        return max(loi)
    middle = int(total / 2)
    peak = loi[middle]
    if peak > loi[middle - 1] and peak > loi[middle + 1]:
        return peak
    elif peak < loi[middle - 1]:
        return find_peak(loi[:middle])
    else:
        return find_peak(loi[middle + 1:])
