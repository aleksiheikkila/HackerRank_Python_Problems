'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/pairs/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    # k: the target difference
    num_found = 0
    arr = sorted(arr)

    # Greedy and naive (not performant enough)
    #num_found = sum(1 
    #        for i, a in enumerate(arr) 
    #        for j, b in enumerate(arr) 
    #        if i != j and a - b == k)
    #
    #return num_found


    for i, elem in enumerate(arr):
        # Bisection approach
        # Divide the array ahead in two parts, check on which part the correct second term of the difference would be located
        # keep dividing. When we are close enough, iterate the part of the array to check if match can be found

        j = i   # index for the bisection
        midpoint_idx = j + ((len(arr) - j - 1) // 2)  # midpoint from the current location to the right end of the array

        while True:
            midpoint_val = arr[midpoint_idx]

            if abs(j-midpoint_idx) < 100:  # close enough, iterate then element by element
                break

            if midpoint_val - elem < k:  # keep searching on the right
                j = midpoint_idx
                midpoint_idx = midpoint_idx + ((len(arr) - midpoint_idx - 1) // 2)
            else:
                midpoint_idx = midpoint_idx - ((midpoint_idx - i) // 2)

        # Iterate element for element, starting for the searched starting location (breaking out as soon as it is clear that no match is found)
        for look_ahead_idx in range(j, len(arr)):   
            elem_ahead = arr[look_ahead_idx]
            if elem_ahead - elem > k:
                break
            elif elem_ahead - elem == k:
                num_found += 1


    return num_found


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
