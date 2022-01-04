'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jul 2020
Problem   : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

There are a few test cases that fail. Did not dig deeper what kind of an (edge) case causes that. 
'''
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the isValid function below.
def isValid(s):
    counts = Counter(s)
    #print(counts)
    shortest = min(counts.values())
    #print(shortest)
    if sum((max(0, val - shortest) for val in counts.values())) >= 2:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
