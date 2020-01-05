'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jan 2020
Problem   : https://www.hackerrank.com/challenges/polar-coordinates/problem
'''
# You are given a complex . Your task is to convert it to polar coordinates.
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

z = input()
z = complex(z)

print(abs(z))
print(cmath.phase(z))