def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for i in range(n)]
mod = pow(10,9)+7
import numpy as np
#import sympy
import math
md = 998244353

n,k = L()
lr = NL(k)
s = set()

for l,r in lr:
    s |= set(range(l,r+1))


dp = [0]*(n+1)
dp[1]=1
#dp[2]=-1
c = [0]*(n+1)
for i in range(1,n+1):
    dp[i] = (dp[i]+dp[i-1])%md
    for l,r in lr:
        if i+l < n+1:
            dp[i+l] += dp[i]
            dp[i+l] %= md
            if i+r+1 < n+1:
                dp[i+r+1] -= dp[i]
                dp[i+r+1] %= md

print((dp[n] - dp[n-1])%md)