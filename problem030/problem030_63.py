from math import *
a,b,c = map(int,raw_input().split())
sinc = sin(radians(c))
cosc = cos(radians(c))
S = 0.5 * a * b * sinc
L = a+b+sqrt(a**2+b**2-2*a*b*cosc)
h = b*sinc
print S
print L
print h