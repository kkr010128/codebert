# import numpy as np
import sys, math, heapq
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial, gcd
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep="\n")

H, W, M = map(int, input().split())
hw = [list(map(int, input().split())) for _ in range(M)]

hb = defaultdict(int)
wb = defaultdict(int)
bomb = defaultdict(int)

for hwi in hw:
    h, w = hwi
    hb[h] += 1
    wb[w] += 1
    bomb[(h, w)] += 1

# print(hb, wb)

mhb = max(hb.values())
mwb = max(wb.values())

maxh = [key for key, val in hb.items() if val == mhb]
maxw = [key for key, val in wb.items() if val == mwb]

# print(maxh, maxw)

for h in maxh:
    for w in maxw:
        if bomb[(h, w)] == 0:
            print(mhb + mwb)
            exit()
print(mhb + mwb - 1)
