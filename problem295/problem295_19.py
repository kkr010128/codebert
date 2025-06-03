import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N, M, L = map(int, input().split())
dist = [[INF] * N for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    if c > L:
        continue
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c
Q = int(input())

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
fuel = [[INF] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        fuel[i][j] = 1 if dist[i][j] <= L else INF
for k in range(N):
    for i in range(N):
        for j in range(N):
            fuel[i][j] = min(fuel[i][j], fuel[i][k] + fuel[k][j])
for i in range(Q):
    s,t = map(int, input().split())
    if fuel[s - 1][t - 1] != INF:
        print(fuel[s - 1][t - 1] - 1)
    else:
        print(-1)