'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jul 2020
Problem   : https://www.hackerrank.com/challenges/fibonacci-modified/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    prev = t2  # the previous term in the series, t**2 term,
    prev2 = t1 # the term before the previous
    for _ in range(n-2):
        new = prev2 + prev**2
        prev2 = prev
        prev = new

    return new

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
