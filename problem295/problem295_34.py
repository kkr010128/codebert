# coding: utf-8
from scipy.sparse.csgraph import floyd_warshall

N,M,L=map(int, input().split())
RG=[[0 for i in range(N)] for j in range(N)]

for i in range(M):
    f,t,c = map(int, input().split())
    if c <= L:
        RG[f-1][t-1] = c
        RG[t-1][f-1] = c

Rd = floyd_warshall(RG, directed=False)

FG=[[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if Rd[i][j] <= L:
            FG[i][j] = 1
            FG[j][i] = 1

Fd = floyd_warshall(FG, directed=False)

Q=int(input())
for i in range(Q):
    s, t = map(int, input().split())
    v = Fd[s-1][t-1]
    if s == t:
        print (str(0))
    if v == float('inf'):
        print (str(-1))
    else:
        print (str(int(v-1)))

