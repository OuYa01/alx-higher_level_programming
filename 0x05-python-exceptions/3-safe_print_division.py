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

        if result > 0:
            return (result)

    except (ZeroDivisionError, ValueError):
        return (None)

    finally:
        if 'result' in locals():
            print("{}".format(result))
        else:
            print(None)
