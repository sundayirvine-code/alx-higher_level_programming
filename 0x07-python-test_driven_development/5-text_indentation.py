#!/usr/bin/python3

"""Defines a text-indentation function"""

def text_indentation(text):
    """prints text with two new lines after each ., ? and :
    Args:
        text(string): The text to print
    Raises:
        TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    temp = ''
    for i in text:
        if i == '.' or i == '?' or i == ':':
            temp.strip()
            print(temp)
            print()
            temp = ''
        else:
            temp += i
    print(temp, end='')
