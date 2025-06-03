#!/usr/bin/python3

def find(id, V, d, dist):
    i = id - 1
    dist[i] = d
    for v in V[i]:
        if dist[v - 1] == -1 or dist[v - 1] > d + 1:
            find(v, V, d + 1, dist)
    
n = int(input())
# [isFind, d, f]
A = [[False, 0, 0] for i in range(n)]
U = []
V = []
dist = [-1] * n
for i in range(n):
    l = list(map(int, input().split()))
    U.append(l[0])
    V.append(l[2:])

find(1, V, 0, dist)

for u in U:
    print(u, dist[u - 1])