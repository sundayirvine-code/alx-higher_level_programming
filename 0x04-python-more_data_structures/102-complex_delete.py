#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_ = a_dictionary.copy()
    for key, val in a_dictionary.items():
        if val == value:
            del dict_[key]
    return dict_
