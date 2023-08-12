#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''
    print_matrix_integer - this function print a matrix of integres
    @matrix: the matrix we want to print
    Return: nothing
    '''
    for row in matrix:
        for i, elemnet in enumerate(row):
            print("{:d}".format(elemnet), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()
