'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jan 2020
Problem   : https://www.hackerrank.com/challenges/iterables-and-iterators/problem
'''

# You are given a list of N lowercase English letters. 
# For a given integer K, you can select any K indices 
# (assume 1-based indexing) with a uniform probability from the list.

# Find the probability that at least one of the  indices selected will contain the letter: 'a'.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as it
import math

def nCr(n, k):
    """number of combinations when selecting k items out of n"""
    f = math.factorial
    return f(n) // f(k) // f(n-k)

N = int(input())
letters = input().split()
K = int(input())

num_combs = nCr(N, K)
num_with_a = len(list(comb for comb in it.combinations(letters, K) 
                        if any(char=="a" for char in comb)))

print(num_with_a / num_combs)
