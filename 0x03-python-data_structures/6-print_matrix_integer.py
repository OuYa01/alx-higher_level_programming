#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''
    print_matrix_integer - this function print a matrix of integres
    @matrix: the matrix we want to print
    Return: nothing
    '''
    for row in matrix:
        for elemnet in row:
            print("{:d}".format(elemnet), end=" ")
        print()
