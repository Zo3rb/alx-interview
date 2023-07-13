#!/usr/bin/python3
"""
0. Minimum Operations.
"""

def minOperations(n=6):
    """
    In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n,
    write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): Number of operations.

    Returns:
        (int): The fewest number of operations to perform.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        if n % factor == 0:
            operations += factor
            n = n // factor
            factor -= 1
        factor += 1

    return operations
