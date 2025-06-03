# -*- coding: utf-8 -*-
import sys
N=int(sys.stdin.readline().strip())
A=map(int, sys.stdin.readline().split())

AA=[]
for i,val in enumerate(A):
    AA.append((val,i+1))

AA.append((float("inf"),None))  #1-indexedにする
AA.sort(reverse=True)

dp=[ [ 0 for r in range(N+1) ] for l in range(N+1) ]
dp[0][0]=0

l=0
for l in range(N):
    for r in range(N-l):
        val,idx=AA[l+r+1][0],AA[l+r+1][1]
        dp[l+1][r]=max( dp[l+1][r], dp[l][r]+abs(val*(idx-l-1)) )
        dp[l][r+1]=max( dp[l][r+1], dp[l][r]+abs(val*(N-r-idx)) )

ans=float("-inf")
for l in dp:
    ans=max(ans,max(l))

print ans