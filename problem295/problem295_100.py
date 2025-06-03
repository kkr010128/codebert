ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
n,m,l = ma()
INF=10**15
cost = [[INF]*n for i in range(n)]
for i in range(m):
    a,b,c = ma();a-=1;b-=1
    cost[a][b]=c
    cost[b][a]=c

def wf(cost):
    l = len(cost[0])
    for k in range(l):
        for i in range(l):
            for j in range(l):
                cost[i][j] =  min(cost[i][j],cost[i][k] + cost[k][j])
wf(cost)
rest = [[INF]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if cost[i][j]<=l:
            rest[i][j]=1
wf(rest)
q = ni()
for i in range(q):
    s,t = ma();s-=1;t-=1
    print(rest[s][t] -1) if rest[s][t] !=INF else print(-1)
