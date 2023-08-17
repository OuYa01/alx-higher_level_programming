#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''
    multiply_by_2 - function that returns a new dictionary
                    with all values multiplied by 2

    @a_dictionary: The initial dictionary

    Return: new dictionary with all values mul by 2
    '''
    new_dic = {}
    for i in a_dictionary:
        new_dic[i] = a_dictionary[i] * 2
    return (new_dic)
