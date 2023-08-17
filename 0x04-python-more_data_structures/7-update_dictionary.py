#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    '''
    update_dictionary - Function that replaces or adds
                        key/value in a dictionary.

    @a_dictionary:The initial dictionary
    @Key: The Key to be updated or add
    "value: The value associted with the key

    Returns: The update dictionary
    '''
    a_dictionary[key] = value
    return (a_dictionary)
