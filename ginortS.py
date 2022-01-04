'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jun 2020
Problem   : https://www.hackerrank.com/challenges/ginorts/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

lowercases = []
uppercases = []
odds = []
evens = []

for char in s:
    if char.isdigit():
        if int(char) % 2 == 0: evens.append(char)
        else: odds.append(char)
    elif char.isupper(): uppercases.append(char)
    elif char.islower(): lowercases.append(char)

output = sorted(lowercases) + sorted(uppercases) + sorted(odds) + sorted(evens)
print("".join(output))