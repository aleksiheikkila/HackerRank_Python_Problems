'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/utopian-tree/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    """
    Complete the utopianTree function.
    It should return the integer height of the tree after the input number of growth cycles.

    utopianTree has the following parameter(s):
    n: an integer, the number of growth cycles to simulate
    """

    # The Utopian Tree goes through 2 cycles of growth every year.
    # Each spring, it doubles in height. Each summer, its height increases by 1 meter.
    # tree begins with h of 1m
    
    h = 1
    for i in range(n):
        if i % 2 == 0:
            h *= 2
        else:
            h += 1

    return h


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
