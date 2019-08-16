#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    """
    Complete the climbingLeaderboard function. 
    It should return an integer array where each element represents Alice's rank after the game.

    climbingLeaderboard has the following parameter(s):

    scores: an array of integers that represent leaderboard scores
    alice: an array of integers that represent Alice's scores
    """

    # unique scores
    scores = sorted(list(set(scores)))  # asc
    player_ranks = []
    idx = 0
    n = len(scores)

    for alice_score in alice:  # alice in asc order
        
        # Find the rank. For next alice score (which is not smaller), continue from the same index
        while (n > idx and alice_score >= scores[idx]):
            idx += 1

        player_ranks.append(n+1-idx)

    return player_ranks



def climbingLeaderboard_other(scores, alice):
    scores = sorted(list(set(scores)))
    index = 0
    rank_list = []
    n = len(scores)
    for i in alice:
        while (n > index and i >= scores[index]):
            index += 1
        rank_list.append(n+1-index) 
    return rank_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
