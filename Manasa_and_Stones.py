'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/manasa-and-stones/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    """Complete the stones function. 
    It should return an array of integers representing all possible values of the last stone, sorted ascending.

    stones has the following parameter(s):

    n: an integer, the number of non-zero stones (it seems that the first stone in included in the n)
    a: one possible integer difference
    b: another possible integer difference
    """
    # Any two consecutive stones' numbers differ by one of two values, a and b

    stones = [[0]]
    for _ in range(n-1):  # add the remaining stones
        new_stone = []    # possible values for the new stone
        for step_size in (a,b):
            new_stone.extend([val + step_size for val in stones[-1]])

        stones.append(sorted(list(set(new_stone))))

    return stones[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
