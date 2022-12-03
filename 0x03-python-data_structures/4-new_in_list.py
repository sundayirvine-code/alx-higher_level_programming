#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    elif idx < 0:
        return my_list.copy()
    elif idx >= len(my_list):
        return my_list.copy()
    else:
        new = my_list.copy()
        new[idx] = element
        return new
