'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/encryption/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools as it

# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ", "")
    L = math.sqrt(len(s))

    floor, ceil = math.floor(L), math.ceil(L)

    # num of rows and cols can be from floor to ceil
    # pick the one where L fits, but which has the smallest area

    smallest_area = float("Inf")
    chosen_num_rows = chosen_num_cols = 0
     

    for num_rows in range(floor, ceil+1):
        for num_cols in range(floor, ceil+1):
            area = num_rows * num_cols
            # fits the data
            if area >= L:
                chosen_num_rows = num_rows
                chosen_num_cols = num_cols
                if area < smallest_area:
                    smallest_area = area
    
    splitted = []
    n = 0
    while n < len(s):
        splitted.append(list(s[n:n+chosen_num_cols]))
        n += chosen_num_cols

    encoded = list(it.zip_longest(*splitted, fillvalue=""))
    encoded = ["".join(sublist) for sublist in encoded]
    encoded = " ".join(encoded)


    return encoded

    # hae and via ecy
    ['have', 'anic', 'eday']

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
