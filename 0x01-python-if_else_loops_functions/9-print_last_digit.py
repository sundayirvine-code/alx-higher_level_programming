#!/usr/bin/python3
def print_last_digit(number):
    s = str(number)
    digit = int(s[-1])
    print("{}".format(digit), end='')
    return digit
