'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/non-divisible-subset/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    """Complete the nonDivisibleSubset function. 
    It should return an integer representing the length of the longest subset of meeting the criteria.

    nonDivisibleSubset has the following parameter(s):

    S: an array of distinct integers
    k: an integer
    """


    # For a sum of two numbers to be evenly divisible by k, the following condition has to hold. 
    # If the remainder of N1 % k == r then N2 % k = k-r for N1+N2 % k == 0. 
    # Let us calculate the set of all numbers with a remainder of r and k-r and pick the larger set of the two 
    # (and none from the other) 
    
    # Special cases:
    # If the remainder is half of k such as 2 % 4 = 2 
    # or exactly k such as 4 % 4 = 0, just one number from each of these sets can be contained in S’.


    numbers_in_remainder_buckets = [0] * k  # for remainders 0, 1, ... k-1

    # calculate how many numbers fall into each bucket
    for num in s:
        numbers_in_remainder_buckets[num % k] += 1

    max_subset_length = 0

    # case remainder zero: we can have only one of these numbers (if there were any)
    if numbers_in_remainder_buckets[0]:
        max_subset_length += 1
    
    # case k is even and  remainder is half of k, can take only one of these nums
    # e.g. k= 4 and got nums 6, 10 both with remainder 2. Cannot take both.
    if k % 2 == 0 and numbers_in_remainder_buckets[k//2]:
        max_subset_length += 1

    # else, the symmetric case: remainder 1 vs k-1, 2 vs k-2, ... n vs k-n. Take the max for each
    for idx in range(1, (k+1)//2):
        max_subset_length += max(numbers_in_remainder_buckets[idx],
                                 numbers_in_remainder_buckets[k-idx])


    return max_subset_length



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
