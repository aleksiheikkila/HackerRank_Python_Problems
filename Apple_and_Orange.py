'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/apple-and-orange/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Complete the countApplesAndOranges function. 
    It should print the number of apples and oranges that land on Sam's house, each on a separate line.

    countApplesAndOranges has the following parameter(s):

    s: integer, starting point of Sam's house location.
    t: integer, ending location of Sam's house location.
    a: integer, location of the Apple tree.
    b: integer, location of the Orange tree.
    apples: integer array, distances at which each apple falls from the tree.
    oranges: integer array, distances at which each orange falls from the tree.
    """

    # where did the fruits land?
    apple_landing_locs = [a + apple for apple in apples]
    orange_landing_locs = [b + orange for orange in oranges]

    # how many landed on the house?
    num_apples_on_house = sum((1 for loc in apple_landing_locs 
                                if loc >= s and loc <= t))

    num_oranges_on_house = sum((1 for loc in orange_landing_locs 
                                if loc >= s and loc <= t))

    # print how many apples, oranges fall on the house
    print(num_apples_on_house)
    print(num_oranges_on_house)

    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
