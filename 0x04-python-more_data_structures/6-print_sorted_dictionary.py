#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''
    print_sorted_dictionary - function that prints a dictionary by ordered keys

    @a_dictionary: is the initial dictionary
    '''
    sorted_keys = sorted(a_dictionary.keys())

    for k in sorted_keys:
        value = a_dictionary[k]
        print("{}: {}".format(k, value))
