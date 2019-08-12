'''
HackerRank problem, Extra Long Factorials
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/extra-long-factorials/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    val = 1
    for i in range(2, n+1):
        val *= i
    print(val)
    #return val

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
