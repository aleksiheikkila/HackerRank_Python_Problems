'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/migratory-birds/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    """Complete the migratoryBirds function. 
    It should return the lowest type number of the most frequently sighted bird.

    migratoryBirds has the following parameter(s):
    arr: an array of integers representing types of birds sighted
    """
    counts =  Counter(arr)

    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[0][0]

    # Alternative could ne most_common(n), but note: Elements with equal counts are ordered arbitrarily

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
