from __future__ import division, print_function
from sys import stdin
from math import hypot, sqrt
x1, y1, x2, y2 = (float(s) for s in stdin.readline().split())
print('{:.4f}'.format(hypot(x1-x2, y1-y2)))