#!/usr/bin/env python3
def no_c(my_string):
    s = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            s += i
    return (s)
