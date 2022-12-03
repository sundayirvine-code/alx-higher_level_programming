#!/usr/bin/python3
def max_integer(my_list=[]):
    l = len(my_list)
    if l == 0:
        return None
    else:
        m = my_list[0]
        for i in my_list:
            if i > m:
                m = i
    return m
