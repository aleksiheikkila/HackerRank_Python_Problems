'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/plus-minus/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    num_neg = num_zero = num_pos = 0
    for num in arr:
        if num < 0:
            num_neg += 1
        elif num > 0:
            num_pos += 1
        else:
            num_zero += 1

    print(num_pos/len(arr))
    print(num_neg/len(arr))
    print(num_zero/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
