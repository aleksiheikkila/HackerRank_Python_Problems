'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2020
Problem   : https://www.hackerrank.com/challenges/larrys-array/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def larrysArray(A):
    # Similar to 15 puzzle problem
    # Count the total nbr of inversions. 
    # If divisible by two --> "YES". Else "NO"
    inversions = sum(sum(1 for v in A[:i] if v > val) for i, val in enumerate(A))
    if inversions % 2 == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
