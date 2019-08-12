'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/angry-children/problem  (maxmin?)
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr = sorted(arr)  # smallest to largest
    
    # take k consecutive numbers, determine range, track best
    min_fairness = float("inf")

    for i in range(len(arr) + 1 - k):
        maxmin = arr[i+k-1] - arr[i]
        if maxmin < min_fairness:
            min_fairness = maxmin

    return min_fairness


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
