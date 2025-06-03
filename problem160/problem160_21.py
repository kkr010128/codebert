import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

n, m, q = rm()
li = [rl() for _ in range(q)]
max_ = 0
for A in list(itertools.combinations_with_replacement(list(range(1, m+1)), n)):
    score = 0
    for abcd in li:
        a, b, c, d = abcd
        a -= 1
        b -= 1
        if A[b] - A[a] == c:
            score += d
    else:
        max_ = max(score, max_)
print(max_)