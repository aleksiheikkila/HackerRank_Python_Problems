'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/sherlock-and-array/problem
'''

# ...find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    # naive approach but with tracking the sums instead of calculating them from scratch every time
    # could also bisect for possible performance boost (in some cases...)
    sum_left = 0 
    sum_right = sum(arr)
    for i in range(len(arr)):
        # current index i. left sum up to i-1, right sum from i+1 to the end
        sum_left += arr[i-1] if i > 0 else 0      
        sum_right -= arr[i]
        if sum_left == sum_right:
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
