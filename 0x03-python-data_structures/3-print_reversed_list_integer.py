#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list) - 1
    while(l >= 0):
        print("{:d}".format(my_list[l]))
        l -= 1
