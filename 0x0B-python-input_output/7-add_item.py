#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""
import sys
import json
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

string = []
n = len(sys.argv)


if os.path.exists("add_item.json"):
    old_string = load_from_json_file("add_item.json")
    string += old_string

for i in range(1, n):
    string.append(sys.argv[i])

save_to_json_file(string, "add_item.json")
