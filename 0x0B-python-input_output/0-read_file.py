#!/usr/bin/python3
'''Module:0-read_file'''
def read_file(filename=""):
    '''Reads a text file and prints contents
    Args:
        filename: path to file to be read
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        print(data)
