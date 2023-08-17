#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    if search in my_list:
        for i in my_list:
            new_list.append(i)
        s = new_list.index(search)
        new_list[s] = replace
        return (new_list)
