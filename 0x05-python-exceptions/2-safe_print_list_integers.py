#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        # try to access the element
        try:
            element = my_list[i]
            # check if element is an integer
            if type(element) is int:
                print("{:d}".format(element), end = '')
                count += 1
        except IndexError:
            raise IndexError
    print()
    return count
