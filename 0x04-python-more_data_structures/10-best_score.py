#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    values = []
    for v in a_dictionary.values():
        values.append (v)
    values.sort()
    biggest = values[-1]
    for key in a_dictionary:
        if a_dictionary[key] == biggest:
            return key
