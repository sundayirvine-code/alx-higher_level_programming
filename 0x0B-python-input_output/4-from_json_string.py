#!/usr/bin/python3
'''Modeule: 4-from_json_string.py'''

import json

def from_json_string(my_str):
    '''t returns an object (Python data structure) 
    represented by a JSON string
    '''
    return json.loads(my_str)
