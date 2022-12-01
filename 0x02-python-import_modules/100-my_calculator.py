#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
def cal():
    l = len(argv) - 1
    if l != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = ['+','-','*','/']
    if argv[2] not in ops:
        print("{}".format('Unknown operator. Available operators: +, -, * and /'))
        exit(1)
    else:
        num1 = int(argv[1])
        num2 = int(argv[3])
        if argv[2] == '+':
            print("{} + {} = {}".format(num1, num2, add(num1, num2)))
        elif argv[2] == '-':
            print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
        elif argv[2] == '*':
            print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
        else:
            print("{} / {} = {}".format(num1, num2, div(num1, num2)))
if __name__ == "__main__":
    cal()
