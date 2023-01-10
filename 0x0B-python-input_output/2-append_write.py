#!/usr/bin/python3
"""Module: 2-append_write"""
def append_write(filename="", text=""):
    ''' appends a string at the end of a text file (UTF8)
    Args:
        filename: file to append to
        text: content to append to file
    Return: number of characters added
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        char_count = f.write(text);
        return char_count
