# -*- coding: utf-8 -*-
# A

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())

if N % 2 == 0:
    print(0.5)
else:
    a = N//2
    b = N - a
    print(b/N)

