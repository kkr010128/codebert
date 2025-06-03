# -*- coding: utf-8 -*-

N = int(raw_input())
A = []
for i in range(N):
    A.append(int(raw_input()))
cnt = 0
G = [1]
while G[-1]*3+1 < N:
    G.append(G[-1]*3+1)
G.reverse()
m = len(G)
for i in range(m):
    g = G[i]
    for j in range(g, N):
        v = A[j]
        k = j-g
        while k >= 0 and A[k] > v:
            A[k+g] = A[k]
            k -= g
            cnt += 1
        A[k+g] = v
print m
print " ".join(map(str, G))
print cnt
for i in range(N):
    print A[i]