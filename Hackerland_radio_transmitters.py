'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
'''


#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    houses = sorted(x)
    num_tx = 0  # this wil be returned
    i = 0
    n = len(houses)
    
    tx_locs = []

    while i < n:  # loop over houses
        num_tx += 1  # place next tx
        loc = houses[i] + k  # radius border. loc is still within reach
        
        # move to first house that would fall outside coverage
        while i < n and houses[i] <= loc:
            i += 1
            
        # add new tx to x[i-1]
        tx_locs.append(i-1)
        
        # then the new border location becomes (still within coverage):
        loc = houses[i-1] + k 
        
        # roll forward, find first house that is not covered (or go past the end of list...)
        while (i < n and houses[i] <= loc):  
            i += 1 

    return num_tx



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
