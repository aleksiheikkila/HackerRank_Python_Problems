
'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jun 2020
Problem   : https://www.hackerrank.com/challenges/matrix-script/problem
'''

import math
import os
import random
import re
import sys

USE_RE_VERSION = True  # "version 2"

if not USE_RE_VERSION:
    import string
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    matrix = []

    VALID_CHARS = string.ascii_lowercase + \
                    string.ascii_uppercase + \
                    string.digits + \
                    "!@#$%&"
    #print(VALID_CHARS)

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    cols = ["".join(list(i)) for i in zip(*matrix)]

    s = "".join(cols)
    l = len(s)

    for idx, char in enumerate(s):
        if char.isalnum(): 
            first_alnum_idx = idx
            break

    for idx, char in enumerate(s[::-1]):
        if char.isalnum(): 
            last_alnum_idx = l - 1 - idx
            break

    prefix = s[:first_alnum_idx]
    post = s[last_alnum_idx+1:]
    body = s[first_alnum_idx:last_alnum_idx+1]

    body = "".join(char if char.isalnum() else " " for char in body)
    body = " ".join(body.split())
    s = prefix + body + post

    print(s)  
    # Solution not accepted... It seems that if statements are strictly not allowed

else: # USE_RE_VERSION. Grader accepts this version
## Version 2 - Without ifs

# Generate the string, then do the necessary replacings using re
s = "".join([matrix[j][i] for i in range(m) for j in range(n)])
pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
# matches those non alnums (greedily, as many chars there are back-to-back)
# between alnums...
# Check: https://stackoverflow.com/questions/14646955/not-able-to-understand-python-regex-with
# for those lookahead/lookback expressions
print(re.sub(pat, ' ', s))

