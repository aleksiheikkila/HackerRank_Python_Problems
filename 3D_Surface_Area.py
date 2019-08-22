'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/3d-surface-area/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    # A: H lines, with W space separated ints

    # each slot in the grid has a bottom and top faces. These give area of 2. Then we need the visible area of the sides
    areas = {(h,w): 2 for h in range(len(A)) for w in range(len(A[0]))}   # key is the slot in the grid. Init with top+bottom
    blocks = {(h,w): A[h][w] for h in range(len(A)) for w in range(len(A[0]))}  # put the input to a dict

    # for each grid slot, check how the height compares to the neighboring slots and calculate the visible area of the sides
    for (h, w), curr_blocks in blocks.items():
        # if the neighbor is at least equally high, no contribution from that side
        # handle the grid border (no neighbors case) by the dict get default value of zero (the height is zero outside the grid)
        visible_areas_sides = sum(max(0, curr_blocks - blocks.get(key, 0))
                                for key in ((h-1, w), (h+1, w), (h, w-1), (h, w+1)))
        
        areas[(h,w)] += visible_areas_sides

    # return the total 3D area
    return sum(areas.values())

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
