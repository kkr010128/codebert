# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N,M=map(int,input().split())
h=list(map(int,input().split()))
edge=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int1,input().split())
    edge[a].append(b)
    edge[b].append(a)
ans=0
for i in range(N):
    for nv in edge[i]:
        if h[nv]>=h[i]:
            break
    else:
        ans+=1
print(ans)