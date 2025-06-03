import sys
import bisect
import math
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from operator import itemgetter

n,s=map(int,readline().split())
a=list(map(int,readline().split()))
mod=998244353
dp=[[0 for j in range(s+1)] for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(s+1):
        dp[i+1][j]+=2*dp[i][j]
        dp[i+1][j]%=mod
        if j+a[i]<=s:
            dp[i+1][j+a[i]]+=dp[i][j]
            dp[i+1][j+a[i]]%=mod
print(dp[n][s])