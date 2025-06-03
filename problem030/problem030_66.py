from sys import stdin
from math import sin, cos, pi, sqrt

a, b, C = [float(x) for x in stdin.readline().rstrip().split()]
S = a*b*sin(C*pi/180)/2
c = sqrt(a**2 + b**2 - 2*a*b*cos(C*pi/180))
L = a+b+c
h = 2*S/a
print(*[S, L, h], sep = "\n")
