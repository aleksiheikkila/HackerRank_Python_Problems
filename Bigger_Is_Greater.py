'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/bigger-is-greater/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    """
    Complete the biggerIsGreater function in the editor below. It should return the    smallest lexicographically higher string possible from the given string or no answer.

    biggerIsGreater has the following parameter(s):
    w: a string (lowercase ascii[a..z].)
    """

    #Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
    # - It must be greater than the original word (comes later in lex. order)
    # - It must be the smallest word that meets the first condition

    w_mod = None   # modified word after swaps

    # We loop from right to left
    # keep track what has been the "largest" char seen so far (it's in the right side)
    max_ord_on_right_tail = float("-Inf")

    for idx in range(len(w)-1, -1, -1):
        # case we are in a point to make a swap
        if ord(w[idx]) < max_ord_on_right_tail:
            # right part contains something to swap. This is done (max) only once
            right_tail = sorted(list(w[idx+1:]))
            smallest_larger_char_in_right_tail = sorted([char for char in right_tail 
                                                    if ord(char) > ord(w[idx])])[0]
            right_tail.remove(smallest_larger_char_in_right_tail)
            right_tail.append(w[idx])
            right_tail.sort()

            # Then sort the right side of the string (after the swapped left side char) to asc order. Then done.
            w_mod = w[:idx] + smallest_larger_char_in_right_tail + "".join(right_tail)

            break

        else:
            # right part does not contain anything to swap. Update the largest char ord seen
            max_ord_on_right_tail = max(max_ord_on_right_tail, ord(w[idx]))

    # All done:
    if not w_mod:
        return "no answer"
    else:
        return w_mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
