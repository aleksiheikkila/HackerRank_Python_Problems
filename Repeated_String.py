'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/repeated-string/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    """
    return num of char "a" in n first chars in infinitely repeating string s
    """
    num_a_in_s = s.count("a")
    num_repeats = math.ceil(n / len(s))
    
    # take (num_repeats - 1) times the full string, plus len_rest first chars of the string
    len_rest = n - (num_repeats-1) * len(s)   # 0

    return num_a_in_s * (num_repeats-1) + s[:len_rest].count('a')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
