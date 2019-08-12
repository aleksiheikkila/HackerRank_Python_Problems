'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/magic-square-forming/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    """
    The problem considers only 3x3 magic squares. Approach:
    There are 8 solutions to the problem. I compare the input against each solution and keep track what the total cost would be 
    to alter the matrix to that specific solution.
    return min of these.
    """
    # magic nbr = n*(n**2 + 1) / 2
    
    s_flat = [s[i][j] for i in range(len(s)) for j in range(len(s))]  # roll out the input matrix rows
    
    # Possible solutions
    all_solutions = [
                    [8, 1, 6, 3, 5, 7, 4, 9, 2],
                    [6, 1, 8, 7, 5, 3, 2, 9, 4],
                    [4, 9, 2, 3, 5, 7, 8, 1, 6],
                    [2, 9, 4, 7, 5, 3, 6, 1, 8],
                    [8, 3, 4, 1, 5, 9, 6, 7, 2],
                    [4, 3, 8, 9, 5, 1, 2, 7, 6],
                    [6, 7, 2, 1, 5, 9, 8, 3, 4],
                    [2, 7, 6, 9, 5, 1, 4, 3, 8]
                    ]
 
    costs = []
    for sol in all_solutions:
        costs.append(sum((abs(s_flat[i]-sol[i]) for i in range(len(s)**2))))
 
    return min(costs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
