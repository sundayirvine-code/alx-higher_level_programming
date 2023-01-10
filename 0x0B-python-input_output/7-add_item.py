#!/usr/bin/python3
''' function that adds all arguments to a Python list, and then save them to a file
'''

import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
from os.path import isfile

data = []
filename = 'add_item.json'
if isfile(filename):
    data = load_from_json_file(filename)

for item in argv[1:]:
    data.append(item)

save_to_json_file(data, filename)
