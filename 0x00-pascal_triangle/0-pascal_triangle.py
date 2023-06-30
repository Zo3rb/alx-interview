#!/usr/bin/python3
"""Implementing Pascal's Triangle. (Mathematical wonder)"""

def pascal_triangle(n: int) -> list[list[int]]:
	"""Generate Pascal's Triangle up to row n.

	Args:
		n (int): The number of rows to generate.

	Returns:
		list[list[int]]: The Pascal's Triangle, represented as a list of lists.
	"""

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
