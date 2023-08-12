#!/usr/bin/python3
def multiple_returns(sentence):
    '''
    multiple_returns - function that returns a tuple with
    the length of a string and its first character

    @sentence:"string we want to return the len and the first char from it

    Return: len of string and first char of string
    '''
    if len(sentence) == 0:
        return (0, "None")
    return (len(sentence), sentence[0])
