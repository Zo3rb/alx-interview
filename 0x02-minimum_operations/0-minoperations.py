#!/usr/bin/env python3
'''0. Minimum Operations'''

def minOperations(n: int):
	'''In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

 	Args:
		n (int): Number of characters.
		Returns: (int): Number of operations.
	 '''
	if n <= 1:
		return 0
		
	operations = 1
	copied = 1
	
	while copied < n:
		if n % copied == 0:
			operations += (n // copied)
			copied *= (n // copied)
		else:
			copied += 1
			operations += 1
	
	return operations
