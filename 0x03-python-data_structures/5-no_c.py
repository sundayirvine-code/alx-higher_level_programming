#!/usr/bin/env python3
def no_c(my_string):
    s = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            s += i
    return s
