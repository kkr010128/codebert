from math import floor
from fractions import Fraction
a,b=map(str,input().split())
a=int(a)
b=Fraction(b)
print(int(a*b))
