#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for index, row in enumerate(new_matrix):
        for index2, col in enumerate(new_matrix):
            new_matrix[index][index2] = row[index2] ** 2
    return new_matrix
