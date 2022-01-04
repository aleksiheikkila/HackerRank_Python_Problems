# https://www.hackerrank.com/challenges/xor-quadruples

#!/bin/python3

import os
import sys

"""
bitwise xor: bit-by-bit, 1 if only one of the corresponding bits
are one, 0 otherwise.

If the numbers are same => XOR = 0
If different => XOR != 0

We get zero if all bit positions are the same
"""

#
# Complete the beautifulQuadruples function below.
#
def beautifulQuadruples(a, b, c, d):
    rst = total = 0
    a,b,c,d, = sorted([a,b,c,d])
    dp = [0] * (0b111111111111 + 1)
    
    # a^b == c^d -> not beautiful 
    # otherwise beautiful

    # check how many c, d combinations there are and store the xor counts
    for ci in range(1, c+1):
        for di in range(ci, d+1):
            total += 1
            dp[ci^di] += 1
            
    for bi in range(1, b+1):
        for ai in range(1, min(bi, a) + 1):
            # for each a, b combination, there are total c, d combinations
            # dp[ai ^ bi] would be the same with c and d and make it ugly.
            rst += (total - dp[ai^bi])
            
        # remove duplicates from dp
        # iterate b and d
        for di in range(bi, d+1):
            dp[bi^di] -= 1
            total -= 1
            
            
    return rst
    
            
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    abcd = input().split()

    a = int(abcd[0])

    b = int(abcd[1])

    c = int(abcd[2])

    d = int(abcd[3])

    result = beautifulQuadruples(a, b, c, d)

    fptr.write(str(result) + '\n')

    fptr.close()
