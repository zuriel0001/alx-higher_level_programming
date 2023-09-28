def find_peak(list_of_integers):
    """
    Finds a peak in list_of_integers.

    Args:
        list_of_integers (list): A list of integers in which to find a peak.

    Returns:
        int or None: The peak element if found, or None if the list is empty or None.
    """

    if list_of_integers is None or list_of_integers == []:
        return None

    start_index = 0
    end_index = len(list_of_integers)
    middle_index = ((end_index - start_index) // 2) + start_index
    middle_index = int(middle_index)

    if end_index == 1:
        return list_of_integers[0]
    if end_index == 2:
        return max(list_of_integers)

    if list_of_integers[middle_index] >= list_of_integers[middle_index - 1] and \
            list_of_integers[middle_index] >= list_of_integers[middle_index + 1]:
        return list_of_integers[middle_index]

    if middle_index > 0 and list_of_integers[middle_index] < list_of_integers[middle_index + 1]:
        return find_peak(list_of_integers[middle_index:])

    if middle_index > 0 and list_of_integers[middle_index] < list_of_integers[middle_index - 1]:
        return find_peak(list_of_integers[:middle_index])

