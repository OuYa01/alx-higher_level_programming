#!/usr/bin/python3
for ascci in range(122, 96, -1):
    alphabet = chr(ascci)
    if (ascci % 2) != 0:
        '#upper case'
        alphabet = alphabet.upper()
    print("{}".format(alphabet), end='')
