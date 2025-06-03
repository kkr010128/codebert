#!/usr/bin/env python3
import sys, math
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**8)
inf = float('inf')
ans=count=0

n,m=map(int,input().split())
A=list(map(int,input().split()))
dp=[inf]*(n+1)
dp[0]=0
for a in A:
    for i in range(a,n+1):
        dp[i]=min(dp[i],dp[i-a]+1)
print(dp[n])

