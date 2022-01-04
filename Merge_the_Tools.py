'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jun 2020
Problem   : https://www.hackerrank.com/challenges/merge-the-tools/problem
'''
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substr = string[i:i+k]
        print("".join(sorted(set(substr), key=substr.index))) 
        # str.index()method returns the idx of a substr inside the string (if found)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)