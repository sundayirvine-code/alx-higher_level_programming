#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    s = str(number)
    digit = int(s[-1]) * -1
else:
    digit = number % 10
if digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, digit))
elif digit == 0:
    print("Last digit of {} is {} and is 0".format(number, digit))
elif digit < 6 and digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, digit))
