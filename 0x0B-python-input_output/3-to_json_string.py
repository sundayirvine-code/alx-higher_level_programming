#!/usr/bin/python3
import json
def to_json_string(my_obj):
    '''returns the JSON representation of an object'''
    json_data = json.dumps(my_obj)
    return json_data
