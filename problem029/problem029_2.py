from sys import stdin
from math import sqrt

x1, y1, x2, y2 = [float(x) for x in stdin.readline().rstrip().split()]
print(sqrt((x2-x1)**2 + (y2-y1)**2))
