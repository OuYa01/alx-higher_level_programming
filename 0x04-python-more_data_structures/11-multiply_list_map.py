#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    '''
    multiply_list_map - function that returns a list with all
    values multiplied by a number

    @my_list: The initial list
    @number: Each value should be multiplied by this number

    Return: the list with all values multiplied by a number
    '''
    mul = list(map(lambda n: n * number, my_list))
    return (mul)
