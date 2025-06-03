from math import *
a,b,C=map(int,raw_input().split())
C = radians(C)

print (0.5)*a*b*sin(C)
print sqrt(a**2+b**2-2*a*b*cos(C)) + a + b
h = b*sin(C)
print h