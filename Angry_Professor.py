'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    """
    Complete the angryProfessor function. 
    It must return YES if class is cancelled, or NO otherwise.
    ...cancel class if fewer than some number of students (k) are on time

    angryProfessor has the following parameter(s):
    k: the threshold number of students
    a: an array of integers representing arrival times
    """

    num_on_time = sum(1 for arr_time in a if arr_time <= 0)
    retval = "YES" if num_on_time < k else "NO"

    return retval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
