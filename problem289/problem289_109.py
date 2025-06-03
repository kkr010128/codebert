import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

a, b, x = rm()
x /= a
if a*b / 2 >= x:
    a = 2*x / b
    print(90 - math.degrees(math.atan(a/b)))
else:
    x = a*b - x
    b = 2*x / a
    print(math.degrees(math.atan(b/a)))











