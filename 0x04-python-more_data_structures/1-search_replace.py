#!/usr/bin/python3

def search_replace(my_list, search, replace):
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
