#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline().strip()

h, w = [int(x) for x in input().split()]
g = [input() for _ in range(h)]
ans = 0
for si in range(h):
    for sj in range(w):
        if g[si][sj] != '#':
            d = [[-1 for j in range(w)] for i in range(h)]
            d[si][sj] = 0
            q = [(si, sj)]
            for i, j in q:
                ans = max(ans, d[i][j])
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < h and 0 <= nj < w and g[ni][nj] != '#' and d[ni][nj] == -1:
                        d[ni][nj] = d[i][j] + 1
                        q.append((ni, nj))
print(ans)  
