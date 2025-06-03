#!/usr/bin/env python3

import sys
input=sys.stdin.readline

mod=998244353

n,k=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(k)]
dp=[0]*(n+1)
dp[1]=1
acum=[0]*(n+1)
for i in range(k):
  l,r=arr[i]
  if 1+l<=n:
    acum[1+l]+=1
  if 1+r+1<=n:
    acum[1+r+1]-=1
for i in range(2,n+1):
  acum[i]+=acum[i-1]
  acum[i]%=mod
  dp[i]=acum[i]
  for j in range(k):
    l,r=arr[j]
    if i+l<=n:
      acum[i+l]+=dp[i]
    if i+r+1<=n:
      acum[i+r+1]-=dp[i]
print(dp[n]%mod)