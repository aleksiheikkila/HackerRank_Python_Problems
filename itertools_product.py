"""https://www.hackerrank.com/challenges/itertools-product/problem
"""
#  Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = [int(elem) for elem in input().split()]
B = [int(elem) for elem in input().split()]

print(*list(product(A, B)))