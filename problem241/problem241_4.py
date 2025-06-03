from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
# INF =  float("inf")
INF = 10**18
import bisect
import statistics
mod = 10**9+7
# mod = 998244353

H, W = list(map(int, input().split()))
S = []
for i in range(H):
    S.append(input())

def bfs(u):
    stack = deque([u])
    visited = set()
    seen = set()
    p = [[INF for j in range(W)] for i in range(H)]
    p[u[0]][u[1]] = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                p[i][j] = -1

    while len(stack) > 0:
        v = stack.popleft()
        ###
        visited.add(v)
        ###

        a = (v[0] + 1, v[1])
        b = (v[0]    , v[1] + 1)
        c = (v[0] - 1, v[1])
        d = (v[0]    , v[1] - 1)

        e = [a, b, c, d]

        for ee in e:
            if ee[0] >= 0 and ee[0] <= H-1 and ee[1] >= 0 and ee[1] <= W-1:
                if S[ee[0]][ee[1]] == ".":
                    if ee not in visited:
                        p[ee[0]][ee[1]] = min(p[ee[0]][ee[1]], p[v[0]][v[1]] + 1)
                        if ee not in seen:
                            stack.append(ee)
                            seen.add(ee)

    ans = 0
    for i in range(H):
        ans = max(ans, max(p[i]))
    return ans

sol = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            sol = max(sol, bfs((i,j)))

print(sol)