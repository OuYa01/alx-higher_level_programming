#!/usr/bin/python3
def uppercase(str):
    for c in str:
        unicd = ord(c)
        if (unicd in range(97, 123)):
            unicd = unicd - 32
        print("{}".format(chr(unicd)), end='')
    print()
