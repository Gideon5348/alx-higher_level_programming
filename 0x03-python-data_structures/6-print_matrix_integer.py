#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column, number in enumerate(row):
            if column != len(row) - 1:
                print("{:d} ".format(number), end="")
            else:
                print("{:d}".format(number))
    return
