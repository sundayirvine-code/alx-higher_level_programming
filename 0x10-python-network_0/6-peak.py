def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers

    Args:
    - list_of_integers: list of integers

    Returns:
    - a peak in the list, or None if the list is empty
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]
    else:
        mid = n // 2
        if list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid + 1:])
        else:
            return list_of_integers[mid]

