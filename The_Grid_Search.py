'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/the-grid-search/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def are_list_contents_identical(list1, list2, x1, y1, x2, y2, dx, dy):
    return all(l1_row[x1:x1+dx] == l2_row[x2:x2+dx] 
                for l1_row, l2_row in zip(list1[y1:y1+dy], list2[y2:y2+dy]))

def gridSearch(G, P):
    """
    Complete the gridSearch function in the editor below. It should return YES if the pattern exists in the grid, or NO otherwise.

    gridSearch has the following parameter(s):
    G: the grid to search, an array of strings
    P: the pattern to search for, an array of string

    """
    if len(P) > len(G) or len(P[0]) > len(G[0]):
        # pattern is larger than the grid
        return "NO"

    dy = len(P)
    dx = len(P[0])

    for y, row in enumerate(G[:-dy + 1]):
        for x, _ in enumerate(row[:-dx + 1]):
            if are_list_contents_identical(G, P, x1=x, y1=y, x2=0, y2=0, dx=dx, dy=dy):
                return "YES"

    # did not return above --> not found
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
