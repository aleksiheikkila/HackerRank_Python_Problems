'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/bomber-man/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
    """Complete the bomberMan function.
    It should return an array of strings that represent the grid in its final state.

    bomberMan has the following parameter(s):
    n: an integer, the number of seconds to simulate
    grid: an array of strings that represents the grid
    """


    # Coordinate scheme: topleft is 0,0
    grid_dict = {(x,y): 3 if elem == 'O' else '.'
                    for y, line in enumerate(grid) 
                    for x, elem in enumerate(line)}
    # could do sparse dict instead but did not bother

    # get grid shape
    max_x = max(key[0] for key in grid_dict.keys())
    max_y = max(key[1] for key in grid_dict.keys())

    # adjancency coordinate deltas
    adj_offsets = [(0,1), (0,-1), (1,0), (-1,0)]

    def remove_adj_bombs(grid, pos):
        x,y = pos
        for (dx,dy) in adj_offsets:
            if (x+dx, y+dy) in grid:  # within grid
                grid[(x+dx, y+dy)] = "."

        return grid


    def grid_to_str(grid):
        """returns a str representation of the grid"""
        grid_str = ""
        for y in range(max_y+1):
            for x in range(max_x+1):
                grid_str += grid_dict[(x,y)] if grid_dict[(x,y)] == "." else "O"
            grid_str += "\n"

        return grid_str


    def get_grid_at_step_n(grid, n):
        """Returns the grid after given timestep n"""
        for step in range(2, n+1):
            #step 1: do nothing

            if step % 2 == 0:
                # Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. 
                # No bombs detonate at this point.
                for pos, elem in grid.items():
                    if elem == ".":
                        grid[pos] = step + 3

            if step % 2 == 1:
                new_grid = grid.copy()
                # any bombs planted exactly three seconds ago will detonate
                for pos, elem in grid.items():
                    if elem == step:  # timer goes off...
                        # the bomb location and the adjacent locations are cleared. No chain reaction occur.
                        new_grid[pos] = "."
                        new_grid = remove_adj_bombs(new_grid, pos)

                grid = new_grid
        
        return grid


    # Some of the test cases have a lot of steps where naive implementation will time out.
    # One can easily observe that the grid state starts to loop. Using this observation we can skip most of the steps.
    if n < 10:
        # just do the naive
        start_time = 2
    else:
        # get grid state after the first detonation (right after step 3)
        # then the state repeats every 4 steps. Use this info to skip to close to the n and go from there to the finish.
        grid_dict = get_grid_at_step_n(grid_dict, 3)
        num_full_cycles_to_skip = (n-3) // 4
        start_time = 3 + 4*num_full_cycles_to_skip + 1  # continue the process from this step
        #print("skip to step:", start_time)

    for step in range(start_time, n+1):
        if step % 2 == 0:
            # Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. 
            # No bombs detonate at this point.
            for pos, elem in grid_dict.items():
                if elem == ".":
                    grid_dict[pos] = step + 3

        if step % 2 == 1:
            new_grid = grid_dict.copy()
            # any bombs planted three (or more - just related to hopping over steps) seconds ago will detonate
            for pos, elem in grid_dict.items():
                if elem <= step:  # timer goes off...
                    new_grid[pos] = "."
                    new_grid = remove_adj_bombs(new_grid, pos)

            grid_dict = new_grid

            
    # return an array of strings that represent the grid in its final state. Replace numbers with 'O'
    ret_arr = []
    for y in range(max_y+1):
        row_str = ""
        for x in range(max_x+1):
            row_str += grid_dict[(x,y)] if grid_dict[(x,y)] == "." else "O"
        ret_arr.append(row_str)

    return ret_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
