'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    """
    Complete the organizingContainers function. It should return a string, either Possible or Impossible.
    organizingContainers has the following parameter(s):
    containter: a two dimensional array of integers that represent the number of balls of each color in each container
    """
    # Implementation notes:
    # Each container will at all times hold the number of balls there are to begin with (only 1:1 swaps are allowed)

    capacities = [sum(row) for row in container]  # container capacities
    num_balls  = [sum(col) for col in zip(*container)]  # how many balls of each type

    # if the capacities match to num_balls (pairs are found), we can do the sort
    if sorted(capacities) == sorted(num_balls):
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
