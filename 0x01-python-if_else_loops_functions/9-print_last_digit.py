#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        s = str(number)
        digit = int(s[-1]) * -1
    else:
        digit = number % 10

    print("{}".format(digit), end='')
    return digit
