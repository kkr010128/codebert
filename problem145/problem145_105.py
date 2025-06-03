#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)
import bisect
import heapq
import itertools
import math
import numpy as np
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from math import gcd
from operator import add, itemgetter, mul, xor
def cmb(n,r,mod):
  bunshi=1
  bunbo=1
  for i in range(r):
    bunbo = bunbo*(i+1)%mod
    bunshi = bunshi*(n-i)%mod
  return (bunshi*pow(bunbo,mod-2,mod))%mod
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n,m = MI()
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = MI()
    graph[a].append(b)
    graph[b].append(a)

dist = [-1]*(n+1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)
ans = [0]*(n+1)
while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        ans[i] = v
        dist[i] = 0
        d.append(i)
print("Yes")
for i in ans[2:]:
    print(i)