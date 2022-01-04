'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jun 2020
Problem   : https://www.hackerrank.com/challenges/word-order/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input().strip())

words = []
for _ in range(n):
    words.append(input().strip())

wordcounts = OrderedDict()

for word in words:
    if word not in wordcounts: wordcounts[word] = 1
    else:                      wordcounts[word] += 1

print(len(wordcounts))
print(" ".join(map(str, wordcounts.values())))