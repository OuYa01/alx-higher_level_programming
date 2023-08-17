#!/usr/bin/python3

def roman_to_int(roman_string):
    '''
    roman_to_int - function that convert roman string to integre
    '''
    roman_to_decimal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    number = 0
    previos_value = 0
    for i in roman_string:
        value = roman_to_decimal[i]
        if value > previos_value:
            number += value - (2 * previos_value)
        else:
            number += value
        previos_value = value
    return (number)
