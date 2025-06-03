import sys
import math
import itertools
import numpy
import collections

rl = sys.stdin.readline

n = int(rl())
se = []
for _ in range(n):
    x, r = map(int, rl().split())
    start, end = x-r, x+r
    se.append([start, end])
se.sort(key=lambda x: x[1])

cur = se[0][0]
cnt = 0
for i in se:
    if cur <= i[0] <= i[1]:
        cur = i[1]
        cnt += 1
print(cnt)