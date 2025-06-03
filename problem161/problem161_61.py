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

a, b, n = map(int, readline().split())

x = min(b - 1, n)
# if b == n:
#     x = b - 1
# if x == 0:
#     print(a)
#     exit()
ans = math.floor((a * x) / b) - a * math.floor(x / b)
print(ans)