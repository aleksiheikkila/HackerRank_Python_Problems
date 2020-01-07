'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jan 2020
Problem   : https://www.hackerrank.com/challenges/compress-the-string/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input()
compressed = ""

for k, g in groupby(s):
# The operation of groupby(): It generates a break or new group every time the value of 
# the key function (omitting it --> key is the element itself) changes.
    compressed += "({}, {}) ".format(len(list(g)), k)

print(compressed.strip())

