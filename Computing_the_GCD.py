"""
    https://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---gcd/problem
    Greatest Common Divisor using Euclid's iterative procedure
"""

def gcd(x,y):
    while True:
        remainder = x % y
        if remainder == 0: return y
        x = y
        y = remainder

# Unit tests
assert gcd(1, 5) == 1  
assert gcd(10, 100) == 10  
assert gcd(22, 131) == 1
assert gcd(38832, 38832) == 38832
assert gcd(168, 180) == 12
assert gcd(2415, 3289) == 23
assert gcd(4278, 8602) == 46
assert gcd(8602, 4278) == 46