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

n, x, y = map(int, readline().split())

dists = [0 for _ in range(n)]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        d = min(abs(i - j), abs(x - i) + 1 + abs(y - j))
        dists[d] += 1
for i in range(1, n):
    print(dists[i])

