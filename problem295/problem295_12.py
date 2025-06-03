def floyd_warshall(G):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j]=min(G[i][j],G[i][k]+G[k][j])

import sys
input=sys.stdin.readline
INF=10**30
N,M,L=map(int,input().split())
dp1=[[INF]*N for i in range(N)]
for i in range(N):
    dp1[i][i]=0
for _ in range(M):
    A,B,C=map(int,input().split())
    A,B=A-1,B-1
    dp1[A][B]=C
    dp1[B][A]=C

floyd_warshall(dp1)

dp2=[[INF]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if i==j:
            dp2[i][j]=0
        else:
            dp2[i][j]=1 if dp1[i][j]<=L else INF
floyd_warshall(dp2)

Q=int(input())
for _ in range(Q):
    s,t=map(lambda x:int(x)-1,input().split())
    print (dp2[s][t]-1 if dp2[s][t]!=INF else -1)