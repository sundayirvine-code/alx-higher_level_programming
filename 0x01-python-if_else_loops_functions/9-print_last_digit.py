#!/usr/bin/python3
def print_last_digit(number):
    digit = number % 10
    print("{}".format(digit), end='')
    return digit
