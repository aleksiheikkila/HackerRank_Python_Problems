'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2020
Problem   : https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # A little bit too heavy
    num_anagram_substrs = 0

    for l in range(1, len(s)):  
        for left_start_pos in range(len(s)-l):
            for right_start_pos in range(left_start_pos+1, len(s)-l+1):
                left = s[left_start_pos:left_start_pos+l]
                right = s[right_start_pos:right_start_pos+l]
                if sorted(left) == sorted(right):
                    num_anagram_substrs += 1
                    
    return num_anagram_substrs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
