#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    for x in a_dictionary:
        keys.append(x)
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
