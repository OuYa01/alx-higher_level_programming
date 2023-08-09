#!/usr/bin/python3
'''
uppercase - function that prints a string in uppercase followed by a new line

@str = string that will be uppercase
'''


def uppercase(str):
    for c in str:
        unicd = chr(ord(c))
        if (unicd in range(97, 123)):
            unicd = chr(unicd - 32)
        print("{}".format(unicd), end='')
    print()
