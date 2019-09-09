'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Sep 2019
Problem   : https://www.hackerrank.com/challenges/absolute-permutation/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    """
    Complete the absolutePermutation function. 
    It should return an integer that represents the smallest lexicographically smallest permutation, or -1 if there is none.
    [Actually it returns a list of ints]

    absolutePermutation has the following parameter(s):
        n: the upper bound of natural numbers to consider, inclusive
        k: the integer difference between each element and its index
    """
    # Approach
    # Loop over the positions
    # For each position, pick based on the first of the following
        # number pos - k (if avail), or
        # number pos + k (if avail)
        # terminate (no such absolute permutation)

    # abs(x-pos) = k
    # So, x-pos = k (if x >= pos ) or x-pos = -k (if x < pos)
    # So, x = pos + k                     x = pos - k
    # The latter gives the smaller x (when it's available), so prefer it

    available_nums = set(range(1, n+1))
    smallest_permutation = []

    for pos in range(1, n+1):
        if pos-k in available_nums:
            smallest_permutation.append(pos-k)
            available_nums.remove(pos-k)
        elif pos+k in available_nums:
            smallest_permutation.append(pos+k)
            available_nums.remove(pos+k)
        else:
            return [-1]

    return smallest_permutation


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
