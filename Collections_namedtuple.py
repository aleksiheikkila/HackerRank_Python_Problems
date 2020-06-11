'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jan 2020
Problem   : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

USE_ALT = True

if not USE_ALT:
    from collections import namedtuple

    students = []

    N = int(input())
    colnames = input().split()
    c_to_idx = {colname: i for i, colname in enumerate(colnames)}

    Student = namedtuple("Student", " ".join(colnames))

    for _ in range(N):
        row = input().split()
        ID = row[c_to_idx["ID"]]
        MARKS = int(row[c_to_idx["MARKS"]])
        NAME = row[c_to_idx["NAME"]]
        CLASS = row[c_to_idx["CLASS"]]

        students.append(Student(ID=ID, 
                                MARKS=MARKS, 
                                NAME=NAME, 
                                CLASS=CLASS))

    avg = sum(student.MARKS for student in students) / len(students)
    print(round(avg, 2))


###################
## ALTernative terse implementation without namedtuple
else:
    N, marks_idx = int(input()), input().split().index("MARKS")
    marks = [int(input().split()[marks_idx]) for _ in range(N)]
    print(round(sum(marks)/N, 2))
