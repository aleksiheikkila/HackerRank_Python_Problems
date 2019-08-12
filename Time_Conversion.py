'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/time-conversion/problem
'''

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hour = int(s[:2])

    if 'AM' in s:
        hour = '00' if hour == 12 else str(hour).rjust(2, '0')
    else:
        hour = '12' if hour == 12 else str(hour+12).rjust(2, '0')
        
    return hour + s[2:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
