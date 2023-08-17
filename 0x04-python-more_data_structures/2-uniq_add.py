#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''
    uniq_add -  function that adds all unique integers in a list
                only once for each integer
    @my_list: the initial list

    Return: the result of sum of all int
    '''
    my_set = set(my_list)
    add = 0
    for i in my_set:
        add += i
    return (add)
