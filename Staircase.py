'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/staircase/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):

    for lvl in range(n, 0, -1):
        print(" " * (lvl - 1) + "#" * (n - lvl +1))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
