'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/cut-the-sticks/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    """
    Complete the cutTheSticks function. 
    It should return an array of integers representing the number of sticks before each cut operation is performed.

    cutTheSticks has the following parameter(s):

    arr: an array of integers representing the length of each stick
    """

    num_stick_before_round = []

    arr = sorted(arr)

    while True:
        num_stick_before_round.append(len(arr))

        if (max(arr) - min(arr) == 0):  # stop criterion
            break
        else:
            shortest = arr.pop(0)
            arr = [num - shortest 
                    for num in arr 
                    if num - shortest != 0]

    return num_stick_before_round



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
