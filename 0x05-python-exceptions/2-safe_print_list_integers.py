#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    '''
    safe_print_list_integres - prints a list of integers
    and returns the count of printed integers.

    @my_list: list we work on
    @x: represents the number of elements to access in my_list

    Return: the count of integers successfully printed
    '''
    try:
        i = 0
        count = 0

        while i < x:
            print("{:d}".format(my_list[i]), end='')
            i += 1
            count += 1
        print()
        return (count)
    except (ValueError, TypeError):
        while i < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                count += 1
            i += 1
        print()
        return (count)
