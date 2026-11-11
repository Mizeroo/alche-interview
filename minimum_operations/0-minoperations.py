#!/usr/bin/python3
"""
Calculate the minimum number of operations
needed to reach n characters.
"""


def minOperations(n):
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n = n // divisor
        else:
            divisor += 1

    return operations
