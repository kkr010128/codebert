from collections import defaultdict, deque
import sys, heapq, bisect, math, itertools, string, queue, copy, time
from fractions import gcd
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7
EPS = 10**-7

n, a, b = map(int, input().split())

ans = n//(a+b)*a + min(n%(a+b), a)
print(ans)