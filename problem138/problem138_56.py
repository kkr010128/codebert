#!/usr/bin/env python
import sys
sys.setrecursionlimit(10**9)
from collections import deque,defaultdict
import heapq
from itertools import combinations
import bisect


mod=998244353
pp=pow(2,mod-2,mod)

n,s=map(int,input().split())
l=list(map(int,input().split()))

dp=[[0 for j in range(s+1)] for i in range(n+1)]
dp[0][0]=pow(2,n,mod)

for i in range(n):
    for j in range(s+1):
        if dp[i][j]>=1:
            if j+l[i]<=s:
                dp[i+1][j+l[i]]+=dp[i][j]*pp# +pow(2,n-1,mod)
                dp[i+1][j+l[i]]%=mod
            dp[i+1][j]+=dp[i][j]
            dp[i+1][j]%=mod
print(dp[-1][-1]%mod)
