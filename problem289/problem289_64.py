import sys
import itertools
# import numpy as np
import time
import math
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, x = map(int, readline().split())

v = a * a * b
s = x / a

if x == v:
    print(0)
    exit()

if x <= v / 2:
    # print(math.degrees(math.atan(2 * s / b / b)))
    print(90 - math.degrees(math.atan(2 * x / a / b / b)))
else:
    print(90 - math.degrees(math.atan(a / (b - (2 * s / a - b)))))

