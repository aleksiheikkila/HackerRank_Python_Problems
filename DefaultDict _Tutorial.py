'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jan 2020
Problem   : https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
grp_A_indices = defaultdict(list)

for i in range(1,n+1):
    grp_A_indices[input()].append(str(i))
    
for i in range(m):
    print (" ".join(grp_A_indices[input()]) or -1)