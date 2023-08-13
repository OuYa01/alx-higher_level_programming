#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''
    divisible_by_2 - function that finds all multiples of 2 in a list.
    @my_list: our list
    Return: Return the list of True/False values indicating whether
    each element is divisible by 2
    '''
    new_list = []
    for i in my_list:
        new_list.append(i % 2 == 0)
    return (new_list)
