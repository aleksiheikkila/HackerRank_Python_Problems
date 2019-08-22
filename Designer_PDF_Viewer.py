'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

from string import ascii_lowercase

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    """
    Complete the designerPdfViewer function. 
    It should return an integer representing the size of the highlighted area.

    designerPdfViewer has the following parameter(s):

    h: an array of integers representing the heights of each letter
    word: a string
    """
    word = word.strip().lower()
    width = len(word)
    letter_to_height_map = {letter: height for letter, height in zip(ascii_lowercase, h)}
    max_h = max(letter_to_height_map[letter] for letter in word)

    return max_h * width
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
