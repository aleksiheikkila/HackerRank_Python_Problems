'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    """
    Complete the jumpingOnClouds function. 
    It should return the minimum number of jumps required, as an integer. 
    """
    # Greedy approach, move as far as possible
    num_jumps = 0
    current_loc = 0

    while current_loc < len(c)-1:
        # case when we are on the prev to last cloud
        if current_loc == len(c)-2: 
            jump_length = 1
            num_jumps += 1
            current_loc += jump_length
        else:  # can jump either one or two clouds
            jump_length = 2 if c[current_loc+2] == 0 else 1
            num_jumps += 1
            current_loc += jump_length

    return num_jumps




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
