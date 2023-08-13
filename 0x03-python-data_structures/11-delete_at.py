#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    '''
    delet_at - function that delete a item in specific position in a list

    @my_list: the list we work on
    @idx: the position of the item we want to remove

    Return: the nwe list
    '''
    if (my_list is not None and 0 <= idx < len(my_list)):
        del my_list[idx]
    return (my_list)
