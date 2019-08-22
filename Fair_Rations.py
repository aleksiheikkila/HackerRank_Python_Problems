'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/fair-rations/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    """
    Complete the fairRations function. It should return an integer that represents the minimum number of loaves required.

    fairRations has the following parameter(s):
    B: an array of integers that represent the number of loaves each persons starts with
    """
    # RULES:
    # Every time you give a loaf of bread to some person, you must also give a loaf of bread to the person immediately 
    # in front of or behind them in the line (i.e. persons i+1 or i-1).

    # After all the bread is distributed, each person must have an even number of loaves.

    # Given the number of loaves already held by each citizen, find and print the minimum number of loaves you must 
    # distribute to satisfy the two rules above. 
    # If this is not possible, print NO.

    num_breads = 0

    # strategy: start from the beginning. Check if element is odd. If yes, give one bread to him + one to the next i+1 person.
    # (do not look back to left).
    # If the last person in the end does not have even nbr of breads => "NO"
    for i in range(len(B)-1):
        if B[i] % 2 != 0:
            # if person i has odd nbr of breads. Give one to him and the following person.
            B[i] += 1
            B[i+1] += 1
            num_breads += 2

    if B[-1] % 2 != 0:
        return "NO"
    else:
        return num_breads


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
