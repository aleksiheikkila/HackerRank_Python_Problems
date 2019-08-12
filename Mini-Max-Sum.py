'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/mini-max-sum/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Python lists are passed as references
# def foo(bar): ...
# If I call foo(bar), I'm merely creating a binding within the scope of foo to the object the argument bar is bound to when the function is called. 
# If bar refers to a mutable object and foo changes its value, then these changes will be visible outside of the scope of the function.

#o n the other hand, if bar refers to an immutable object, the most that foo can do is create a name bar in its local namespace and bind it to some other object.
# (does not change the original then)

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)  # grab a copy, ascending
    print(str(sum(arr[:-1])) + " " + str(sum(arr[1:])))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

