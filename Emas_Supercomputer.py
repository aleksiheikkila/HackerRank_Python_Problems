'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jul 2020
Problem   : https://www.hackerrank.com/challenges/two-pluses/problem
Added a quick and hacky fix...
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def twoPluses(grid):

    def pluses_overlap(p1, p2):  # (x2,y2,area2)
        # ord: 1= single point, 2= area 5
        plus_one_pts = set()

        x1,y1,area1 = p1
        x2,y2,area2 = p2
        ord1 = int(0.25*(area1-1) + 1)
        ord2 = int(0.25*(area2-1) + 1)

        for dx in range(ord1):
            plus_one_pts.add((x1-dx, y1))
            plus_one_pts.add((x1+dx, y1))

        for dy in range(ord1):
            plus_one_pts.add((x1, y1-dy))
            plus_one_pts.add((x1, y1+dy))

        for dx in range(ord2):
            if (x2-dx, y2) in plus_one_pts: return True
            if (x2+dx, y2) in plus_one_pts: return True

        for dy in range(ord2):
            if (x2, y2-dy) in plus_one_pts: return True
            if (x2, y2+dy) in plus_one_pts: return True
 
        return False


    def get_max_area_for_pos(grid, x, y):

        area = 0
        if grid.get((x,y)) is not None:  # is good
            steps = 1
            while True:
                if (grid.get((x-steps,y)) is None or
                    grid.get((x+steps,y)) is None or
                    grid.get((x,y+steps)) is None or
                    grid.get((x,y-steps)) is None):
                    #  grid order is steps
                    break

                steps += 1
            area = 1 + 4*(steps-1)

        return area

    #print(grid)
    good_grid = {(colno, rowno): elem for rowno, row in enumerate(grid) for colno, elem in enumerate(row) if elem == "G"}
    #print(good_grid)

    #print(get_max_area_for_pos(good_grid, 0, 0))  # 0
    #print(get_max_area_for_pos(good_grid, 4, 2))  # 0
    #print(get_max_area_for_pos(good_grid, 3, 1))  # 0

    pluses = []

    for (x,y) in good_grid.keys():
        max_area = get_max_area_for_pos(good_grid,x,y)
        order = int(0.25*(max_area-1) + 1)
        areas = [1 + 4*i for i in range(order)]
        assert areas[-1] == max_area

        for area in areas:
            pluses.append((x,y, area))
        #pluses.append((x,y, get_max_area_for_pos(good_grid,x,y)))
    
    pluses.sort(key=lambda x: x[2], reverse=True)
    print(pluses)

    # search for the biggest two pluses that are compatible
    max_prod = 0
    for i, plus1 in enumerate(pluses):
        for plus2 in pluses[i+1:]:
            area_prod = plus1[2] * plus2[2]
            if area_prod <= max_prod: break
            if not pluses_overlap(plus1, plus2):
                max_prod = area_prod

    return max_prod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)
    fptr.write(str(result) + '\n')
    fptr.close()
