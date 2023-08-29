#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''
    safe_print_list - function that prints from a list up to specified index.

    @my_list: list can contain any type (integre, string, ect)

    @x: represents the number of elements to print
        x can be bigger than the lenght of list

    Return: the real number of elements printed

    Description:

    This function prints items from the provided list up to a given index. It
    carefully manages errors that might occur if the index is out of range.
    '''

    try:
        i = 0
        count = 0
        while i < x:
            print(my_list[i], end='')
            i += 1
            count += 1
        print()
        return (count)

    except IndexError:
        leng = 0

        for _ in my_list:
            leng += 1

        while i < leng:
            print(my_list[i], end='')
            i += 1
            count += 1
        print()
        return (count)
