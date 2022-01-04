'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jun 2020
Problem   : https://www.hackerrank.com/challenges/no-idea/problem
'''

n, m = [int(elem) for elem in input().split()]
arr = [int(elem) for elem in input().split()]
A = set(int(elem) for elem in input().split())
B = set(int(elem) for elem in input().split())
# A and B disjoint: Do not have common elements

happiness = 0

for num in arr:
    if num in A: happiness += 1
    elif num in B: happiness -= 1

print(happiness)
