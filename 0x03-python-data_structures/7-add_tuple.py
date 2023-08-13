#!/usr/bin/pyhon3
def add_tuple(tuple_a=(), tuple_b=()):
    '''
    add_tuple - function that adds 2 tuples

    @tuple_a: the tupl1 that we want to add to tuple2
    @tuple_b: the tuple 2 that we want to add to tuple1

    Return: the sum of tuple_a and tuple_b
    '''
    sum_tuple = ()
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    sum_tuple = a[0] + b[0], a[1] + b[1]
    return (sum_tuple)
