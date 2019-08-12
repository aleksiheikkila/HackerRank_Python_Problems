'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/day-of-the-programmer/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year < 1918:  # case pre 1918: Julian calendar
        leapday = 1 if year % 4 == 0 else 0
        return str(13-leapday) + ".09." + str(year)
    elif year == 1918:  # year 1918, calendar switch (not a leap year)
        return "26.09.1918"
    else:  # after 1918: Gregorian calendar
        leapday = 1 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 0
        return str(13-leapday) + ".09." + str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
