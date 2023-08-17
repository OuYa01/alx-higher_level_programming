#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''
    search_replace - function that replaces all occurrences of
    an element by another in a new list

    @my_list:  is the initial list
    @search: is the element to replace in the list
    @replace: is the new element

    Return: new_list if the element we search its in the list
            my_list if not
    '''
    new_list = []
    if search in my_list:
        for i in my_list:
            new_list.append(i)

        for n in range(len(new_list)):
            if new_list[n] == search:
                new_list[n] = replace

        return (new_list)
    else:
        return (my_list)
