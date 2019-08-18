'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    """
    Complete the divisibleSumPairs function. 
    It should return the integer count of pairs meeting the criteria.

    divisibleSumPairs has the following parameter(s):

    n: the integer length of array
    ar: an array of integers
    k: the integer to divide the pair sum by
    """

    valid_pairs = [[i, j] for i in range(n)
                         for j in range(i+1, n)
                         if (ar[i] + ar[j]) % k == 0]

    return len(valid_pairs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
