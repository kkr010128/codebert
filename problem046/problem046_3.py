from sys import stdin
from math import pi

r = float(stdin.readline().rstrip())
area = pi*r*r
circumference = 2*pi*r
print("%lf %lf" % (area, circumference))
