# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=998244353
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N,S=map(int,input().split())
A=tuple(map(int,input().split()))
dp=[[0]*3001 for _ in range(N+1)]
dp[0][0]=1
for i in range(N):
    for j in range(3001):
        dp[i+1][j]+=dp[i][j]*2
        dp[i+1][j]%=MOD
        if j-A[i]>=0:
            dp[i+1][j]+=dp[i][j-A[i]]
            dp[i+1][j]%=MOD
print(dp[-1][S])