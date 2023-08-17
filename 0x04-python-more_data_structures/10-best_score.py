#!/usr/bin/python3

def best_score(a_dictionary):
    '''
    best_score - function that returns a key with the biggest integer value

    @a-dictionary: The initial dictionary

    Return: the max value in dictionary
            if not a dictionary ret None
    '''
    if not a_dictionary:
        return (None)
    else:
        return (max(a_dictionary.keys()))
