'''
HackerRank problem
Domain    : Python
Author    : Aleksi Heikkilä
Created   : Jun 2020
Problem   : https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
'''
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(self.real*no.real - self.imaginary*no.imaginary,
                       self.real*no.imaginary + self.imaginary*no.real)

    def __truediv__(self, no):
        conjug = Complex(no.real, -no.imaginary)
        denom = (no * conjug).real
        nomin = self * conjug
        return Complex(nomin.real/denom, nomin.imaginary/denom)

    def mod(self):
        return Complex((self.real**2 + self.imaginary**2)**0.5, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':