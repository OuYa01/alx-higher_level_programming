#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    '''
    simple_delete - function that deletes a key in a dictionary

    @a_dictionary: is the intial dictionary
    @key: the key we want to delete

    Return: if key in dictionary return dictionary after updates
            If a key doesn’t exist, return the dictionary with no change
    '''
    if key in a_dictionary:
        del a_dictionary[key]
        return (a_dictionary)
    else:
        return (a_dictionary)
