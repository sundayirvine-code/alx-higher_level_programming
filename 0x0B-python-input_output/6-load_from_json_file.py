#!/usr/bin/python3
''' function that returns an object from a JSON FILE
'''

import json


def load_from_json_file(filename):
    ''' module that creates an Object
     from a “JSON file
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
