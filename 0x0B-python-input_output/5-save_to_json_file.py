#!/usr/bin/python3
''' a function that writes an Object to a text file, using a JSON representation:
'''

import json

def save_to_json_file(my_obj, filename):
    ''' module save_to_json_file
     saves object to file as json representation
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.loads(my_obj))
