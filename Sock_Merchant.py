'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Oct 2019
Problem   : https://www.hackerrank.com/challenges/sock-merchant/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    """
    Complete the sockMerchant function . It must return an integer representing the number of matching pairs of socks that are available.
    sockMerchant has the following parameter(s):

    n: the number of socks in the pile
    ar: the colors of each sock
"""
    num_pairs = 0

    counts = {}
    for sock in ar:
        counts[sock] = counts.get(sock, 0) + 1

    for count in counts.values():
        num_pairs += count // 2

    return num_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
