# -*- coding: utf-8 -*-
# E

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

n = int(input())
d1 = [] * n
d2 = [] * n

for i in range(n):
    x, y = map(int, input().split())
    d1.append(x+y)
    d2.append(x-y)

print(max(max(d1) - min(d1), max(d2)-min(d2)))
