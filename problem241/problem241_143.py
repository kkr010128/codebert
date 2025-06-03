from collections import defaultdict, deque
import sys, heapq, bisect, math, itertools, string, queue, copy, time
from fractions import gcd
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7
EPS = 10**-7

h, w = map(int, input().split())
ini_grid = []
ans = 0
for i in range(h):
    s = list(input())
    ini_grid.append(s)

dd = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(h):
    for j in range(w):
        if ini_grid[i][j] == '.':
            temp_grid = [row[:] for row in ini_grid]
            dis_grid = [[-1]*w for i in range(h)]
            dis_grid[i][j] = 0
            dq = deque([(i, j, 0)])
            temp_grid[i][j] = '#'
            while dq:
                curr = dq.popleft()
                for di, dj in dd:
                    ni = curr[0] + di
                    nj = curr[1] + dj 
                    if (0 <= ni <= h-1) and (0 <= nj <= w-1) and temp_grid[ni][nj] == '.':
                        temp_grid[ni][nj] = '#'
                        dis_grid[ni][nj] = curr[2] + 1
                        dq.append((ni, nj, curr[2] + 1))
                        if curr[2] + 1 > ans:
                            ans = curr[2] + 1

print(ans)