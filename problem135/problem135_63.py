from math import floor 
from fractions import Fraction

A, B = input().split()
A = int(A)
B = Fraction(B)
print(floor(A*B))