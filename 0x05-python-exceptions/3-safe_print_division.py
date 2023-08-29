#!/usr/bin/python3

def safe_print_division(a, b):
    '''
    safe_print_division: function that divides 2 integers and prints the result

    @a: parameter a
    @b: parameter b

    Return: the value of the division, otherwise: None
    '''
    try:
        result = a / b

    except (ZeroDivisionError, ValueError):
        result = None

    finally:
        print("Inside result: {}".format(result))
        return (result)
