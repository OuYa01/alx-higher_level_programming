#!/usr/bin/python3
"""Creating a function"""


def class_to_json(obj):
    """
    function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    my_dir = {}
    attributes = dir(obj)

    for name in attributes:

        if name.startswith("__"):
            continue

        att_val = getattr(obj, name)

        if isinstance(att_val, (int, str, bool)):
            my_dir[name] = att_val

        elif isinstance(att_val, (list)):
            my_dir[att_val] = []

            for item in att_val:
                my_dir[name].append(item)
        elif isinstance(att_val, dict):
            my_dir[name] = {}
            for key, value in att_value.items():
                my_dir[name][key] = value
    return my_dir
