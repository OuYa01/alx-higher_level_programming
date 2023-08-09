#!/usr/bin/python3
'''
uppercase - function that prints a string in uppercase followed by a new line

@str = string that will be uppercase
'''


def uppercase(str):
    for c in str:
        unicd = ord(c)
        '#check if the char is lower case 97 = a and 122 = z'
        if (unicd in range(97, 123)):
            unicd = unicd - 32
        print("{}".format(chr(unicd)), end='')
    print()
