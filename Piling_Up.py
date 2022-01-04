'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jun 2020
Problem   : https://www.hackerrank.com/challenges/piling-up/problem
'''
from collections import deque

num_testcases = int(input())

for case_nbr in range(num_testcases):
    num_cubes = int(input())
    cubes = deque(int(side) for side in input().split())

    size_top = float("Inf")
    stackable = "Yes"

    # Strategy: pick the largest possible
    for i in range(num_cubes):
        if cubes[0] >= cubes[-1]:
            next_cube = cubes.popleft()
        else:
            next_cube = cubes.pop()
        if next_cube > size_top:
            stackable = "No"
            break
        size_top = next_cube

    print(stackable)
