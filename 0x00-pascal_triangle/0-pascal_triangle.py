#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = [[1]]
	if n <= 1:
		return triangle

	for row in range(1, n):
		cur_row = []
		for col in range(row + 1):
			if col == 0 or col == row:
				cur_row.append(1)
			else:
				prev_row = triangle[row - 1]
				cur_row.append(prev_row[col - 1] + prev_row[col])
		triangle.append(cur_row)

	return triangle
