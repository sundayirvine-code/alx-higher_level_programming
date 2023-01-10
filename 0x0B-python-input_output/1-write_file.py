#!/usr/bin/python3
'''Module: 1-write_file'''
def write_file(filename="", text=""):
    '''writes a string to a text file (UTF8) 
    Args:
        filename: File to write to
        text: Contet to write to file
    Return: number of characters written
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        char_count = f.write(text)
        return char_count
