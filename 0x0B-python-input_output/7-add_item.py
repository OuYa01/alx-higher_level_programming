#!/usr/bin/python3
"""Creating a function"""
import sys
import json
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

string = []
n = len(sys.argv)


for i in range(1, n):
    string.append(sys.argv[i])

if os.path.exists("add_item.json"):
    old_string = load_from_json_file("add_item.json")
    string += old_string

save_to_json_file(string, "add_item.json")
