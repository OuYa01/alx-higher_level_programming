#!/usr/bin/python3
def max_integer(my_list=[]):
    '''
    max_integer - function that finds the biggest integer of a list
    @my_list: our list
    Return: biggest integer in list
    '''
    if len(my_list) == 0:
        return (None)
    my_list.sort()
    max_v = my_list[-1]
    return (max_v)
