#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if not matrix:
      return None

    # using list comprehension
    return [[a*a for a in matrix_list] for matrix_list in matrix]
