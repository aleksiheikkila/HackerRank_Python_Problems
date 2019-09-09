'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Sep 2019
Problem   : https://www.hackerrank.com/challenges/queens-attack-2/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    """Complete the queensAttack function. It should return an integer that describes the number of squares the queen can attack.

    queensAttack has the following parameters:
    - n: an integer, the number of rows and columns in the board
    - k: an integer, the number of obstacles on the board
    - r_q: integer, the row number of the queen's position
    - c_q: integer, the column number of the queen's position
    - obstacles: a two dimensional array of integers where each element is an array of integers, the row and column of an obstacle 
    """

    # 8 directions
    # traverse each until obstackle or out of board
    # set of obstacles
    obs = {(x,y) for (x,y) in obstacles}

    # coordinate system. bottom left = (1,1). Let x be the width axis, y height.
    DIRECTIONS = ["UP", "UPRIGHT", "RIGHT", "DOWNRIGHT", "DOWN", "DOWNLEFT", "LEFT", "UPLEFT"]

    # single step dx,dy in different directions
    STEPS = {"UP": (0,1), "UPRIGHT": (1,1), "RIGHT": (1,0), "DOWNRIGHT": (1,-1),
            "DOWN": (0,-1), "DOWNLEFT": (-1,-1), "LEFT": (-1,0), "UPLEFT": (-1, 1)
            }

    num_reachable_squares = 0

    for direc in DIRECTIONS:
        dx, dy = STEPS[direc]
        step_num = 1
        while True:
            curr_x = r_q + step_num * dx
            curr_y = c_q + step_num * dy

            # if out of board or stumbled into an obstacle, stop traversing this direction
            if (curr_x < 1 or curr_x > n 
                or curr_y < 1 or curr_y > n 
                or (curr_x, curr_y) in obs):
                break

            else:
                num_reachable_squares += 1
                step_num += 1

    return num_reachable_squares


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
