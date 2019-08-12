'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/greedy-florist/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    """
    # c: an array of integers representing the original price of each flower
    # k: nbr of friends
    """

    flower_prices = sorted(c)
    flowers_bought = [0 for person in range(k)]   # how many flowers each has bought

    total_cost = 0

    # Start from the most expensive
    # Pick buyer with the least flowers bought so far
    # Calculate cost
    for rnd in range(len(flower_prices)):
        flowers_bought.sort()  # from smallest to largest
        total_cost += (flowers_bought[0] + 1) * flower_prices.pop()
        flowers_bought[0] += 1

    return total_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
