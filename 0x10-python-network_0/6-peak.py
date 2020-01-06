#!/usr/bin/python3
""" Write a function that finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """ Find a peak in a list of unsorted integers """
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    peak = list_of_integers[0]
    diff = max(0, list_of_integers[0] - list_of_integers[1])

    for x in range(1, len(list_of_integers)):
        if list_of_integers[x] - list_of_integers[x - 1] > diff:
            peak = list_of_integers[x]
            diff = list_of_integers[x] - list_of_integers[x - 1]
        if len(list_of_integers) - x > 1:
            if list_of_integers[x] - list_of_integers[x + 1] > diff:
                peak = list_of_integers[x]
                diff = list_of_integers[x] - list_of_integers[x + 1]
    return peak
