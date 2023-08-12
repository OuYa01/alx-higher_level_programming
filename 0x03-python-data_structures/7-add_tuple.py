#!/usr/bin/pyhon3
def add_tuple(tuple_a=(), tuple_b=()):
    '''
    add_tuple - function that adds 2 tuples

    @tuple_a: the tupl1 that we want to add to tuple2
    @tuple_b: the tuple 2 that we want to add to tuple1

    Return: the sum of tuple_a and tuple_b
    '''
    sum_tuples = ()
    if (len(tuple_a) < 1):
        a1, a2 = 0, 0
    elif (len(tuple_a) < 2):
        a1 = int(tuple_a[0])
        a2 = 0
    else:
        a1 = int(tuple_a[0])
        a2 = int(tuple_a[1])

    if (len(tuple_b) < 1):
        b1, b2 = 0, 0
    elif (len(tuple_b) < 2):
        b1 = int(tuple_b[0])
        b2 = 0
    else:
        b1 = int(tuple_b[0])
        b2 = int(tuple_b[1])

    sum_tuples = a1 + b1, a2+ b2
    return (sum_tuples)
