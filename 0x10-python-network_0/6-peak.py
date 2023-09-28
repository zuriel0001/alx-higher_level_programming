def find_peak(list_of_integers):
    """
    Finds a peak in list_of_integers.

    Args:
        list_of_integers (list): A list of integers in which to find a peak.

    Returns:
        int or None: The peak element if found, or
        None if the list is empty or None.
    """

    if list_of_integers is None or list_of_integers == []:
        return None

    start = 0
    end = len(list_of_integers)
    mid = (end - start) // 2 + start
    mid = int(mid)

    if end == 1:
        return list_of_integers[0]
    if end == 2:
        return max(list_of_integers)

    if list_of_integers[mid] >= list_of_integers[mid - 1] and \
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
