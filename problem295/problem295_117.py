#!/usr/bin/pypy
# coding: utf-8

N,M,L=map(int, raw_input().split())
RG=[[ 0 if i==j else float('inf') for i in range(N)] for j in range(N)]

for i in xrange(M):
    f,t,c = map(int, raw_input().split())
    if c <= L:
        RG[f-1][t-1] = c
        RG[t-1][f-1] = c

for k in xrange(N):
    for i in xrange(N):
        for j in xrange(i, N):
            t = RG[i][k] + RG[k][j]
            if RG[i][j] > t:
                RG[i][j] = t
                RG[j][i] = t

FG=[[float('inf') for i in range(N)] for j in range(N)]
for i in xrange(N):
    for j in xrange(i, N):
        if RG[i][j] <= L:
            FG[i][j] = 1
            FG[j][i] = 1

for k in xrange(N):
    for i in xrange(N):
        for j in xrange(i, N):
            t = FG[i][k] + FG[k][j]
            if FG[i][j] > t:
                FG[i][j] = t
                FG[j][i] = t

Q=int(raw_input())
for i in xrange(Q):
    s, t = map(int, raw_input().split())
    v = FG[s-1][t-1]
    if v == float('inf'):
        print (str(-1))
    else:
        print (str(int(v-1)))