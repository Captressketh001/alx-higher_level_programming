#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	if not matrix:
		return None
	return [[a*a for a in num_list] for num_list in matrix]
