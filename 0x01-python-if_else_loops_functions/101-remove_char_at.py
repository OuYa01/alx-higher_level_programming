#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for i, char in enumerate(str):
        if (i != n):
            string = string + char
    return (string)
