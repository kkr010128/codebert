#!/usr/bin/env python3

N, M, L = [int(s) for s in input().split()]
edge = [[int(s) for s in input().split()] for _ in range(M)]
dist = [[10 ** 10] * N for _ in range(N)]
graph = [[] for _ in range(N)]
Q = int(input())

for i, j, w in edge:
    dist[i - 1][j - 1] = w
    dist[j - 1][i - 1] = w

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(N):
    for j in range(N):
        dist[i][j] = 1 if dist[i][j] <= L else 10 ** 10

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


for _ in range(Q):
    s, t = [int(a) - 1 for a in input().split()]
    print(dist[s][t] - 1 if dist[s][t] < 10**10 else -1)