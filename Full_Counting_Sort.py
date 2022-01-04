'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jul 2020
Problem   : https://www.hackerrank.com/challenges/countingsort4/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    sorted_arr = [[] for _ in range(len(arr))]

    for i, (idx, stri) in enumerate(arr):
        if i < 0.5*len(arr): stri = "-"
        sorted_arr[int(idx)].append(stri)
    
    print(" ".join(elem for sublist in sorted_arr for elem in sublist))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
