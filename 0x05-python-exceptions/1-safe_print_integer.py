#!/use/bin/python3

def safe_print_integer(value):
    '''
    safe_print_integer - Safely prints an integer and returns success status
                        Prints the given integer value using the "{:d}"
                        format specifier
    @value: the value to printed
    Return: True if printed scc else return false
    '''
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)
