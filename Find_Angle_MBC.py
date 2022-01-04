'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jun 2020
Problem   : https://www.hackerrank.com/challenges/find-angle/problem
'''
from math import pi, atan

AB = float(input())
BC = float(input())

# midpoint on the hypotenuse divides the right angled triangle in two isosceles triangles
# (An isosceles triangle is a triangle with (at least) two equal sides)
# --> angle(MBC) = angle(MCB)
# --> solve for angle MCB
angle = int(round(atan(AB/BC) * (180/pi), 0))
print(str(angle) + "°")