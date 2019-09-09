'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Aug 2019
Problem   : https://www.hackerrank.com/challenges/bear-and-steady-gene/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


no_of_chars = 256  # sets the list size... should be enough for max ord(char)


# Function to find smallest window containing all characters of 'pat'. Returns the substr  
def findSubString(string, pat):
  
    len1 = len(string)
    len2 = len(pat)
  
    # check if string's length is less than pattern's length. If yes then no such window can exist
    if len1 < len2:  
        print("No such window exists")
        return ""  
  
    hash_pat = [0] * no_of_chars  # occurences of chars in pattern
    hash_str = [0] * no_of_chars  # occurences of chars in string
  
    # store occurrence of characters of pattern
    for i in range(0, len2):  
        hash_pat[ord(pat[i])] += 1
  
    start, start_index, min_len = 0, -1, float('inf')  
  
    # start traversing the string
    count = 0 # count of characters
    for j in range(0, len1):

        # count occurrence of characters of string
        hash_str[ord(string[j])] += 1
  
        # If string's char matches with  
        # pattern's char then increment count  
        if (hash_pat[ord(string[j])] != 0 and
            hash_str[ord(string[j])] <= hash_pat[ord(string[j])]):  
            count += 1
  
        # if all the characters in the pattern are matched  
        if count == len2:  
            # Try to minimize the window i.e., check if  
            # any character is occurring more no. of times  
            # than its occurrence in pattern, if yes  
            # then remove it from starting and also remove  
            # the useless characters.  
            while (hash_str[ord(string[start])] > hash_pat[ord(string[start])] or
                   hash_pat[ord(string[start])] == 0):  # i.e. no need for the char in start index
              
                if (hash_str[ord(string[start])] > hash_pat[ord(string[start])]):
                    hash_str[ord(string[start])] -= 1
                start += 1
              
            # update window size  
            len_window = j - start + 1
            if min_len > len_window:
                min_len = len_window
                start_index = start
  
    # String traversed. If no window found  
    if start_index == -1: 
        print("No such window exists")  
        return ""  
      
    # Return substring starting from  
    # start_index and length min_len  
    return string[start_index : start_index + min_len]  

# Complete the steadyGene function below.
def steadyGene(gene):
    """
    Complete the function. It should return an integer that represents the length of the smallest substring to replace.

    steadyGene has the following parameter:
    gene: a string
    """
    NUCLEOTIDES = {"A", "C", "G", "T"}
    n = len(gene)

    counts = Counter(gene)
    req_changes = {nucleotide: n/4 - counts[nucleotide] for nucleotide in NUCLEOTIDES}

    to_be_removed = {nuc: num for nuc, num in req_changes.items() if num < 0}
    min_num_chars_to_replace = sum(val for val in req_changes.values() if val > 0)
    assert sum(val for val in req_changes.values()) == 0

    pattern_str = "".join([char*int(-num) for char, num in to_be_removed.items()])
    print("pattern:", pattern_str)

    # need to find the shortest substring of gene that contains chars in "pattern_str"
    substr = findSubString(gene, pattern_str)
    assert len(substr) >= min_num_chars_to_replace

    return len(substr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
