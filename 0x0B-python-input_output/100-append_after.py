#!/usr/bib/python3
def append_after(filename="", search_string="", new_string=""):
    content = ''

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            #if line contains search string
            if search_string in line:
                content += line
                content += new_string
            else:
                content += line

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
