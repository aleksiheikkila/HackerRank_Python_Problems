'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jan 2020
Problem   : https://www.hackerrank.com/challenges/maximize-it/problem
'''

# You have to pick one element from each list (K total) so that the value from the equation below is maximized:
# S = (elem1**2 + elem2**2 + ... + elemK**2) % M

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as it

def S(M, *args):
    """Calc function S value"""
    S_sum = 0
    for num in args: 
        S_sum += num**2
    
    return S_sum % M


# Read the inputs in:
K, M = input().split()
K, M = int(K), int(M)

lists = []

for i in range(K):
    row = input().split()
    #Ni = int(row[0]),
    l = [int(elem) for elem in row[1:]]
    lists.append(l)

# We need cartesian product, but in a combination kind of a sense: order does not matter for func S
# --> Cartesian product, only uniques of those
prods = set(it.product(*lists))
S_max = max(S(M, *prod) for prod in prods)

print(S_max)
