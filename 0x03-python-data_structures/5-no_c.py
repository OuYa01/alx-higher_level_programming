#!/usr/bin/python3
def no_c(my_string):
    '''
    no_c - function that removes all characters c and C from a string
    @my_string: the string we want to print
    Return: the new_string that has no c or C
    '''
    if my_string is not None:
        new_string = ""
        for i in my_string:
            if (i == "c" or i == "C"):
                continue
            new_string += i
        return (new_string)
