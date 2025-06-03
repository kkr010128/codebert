import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

# 個数制限なしナップサック問題
W,N = map(int,readline().split())

dp = [INF]*(W+1)
dp[0] = 0

for i in range(N):
    w,v = map(int,readline().split())
    # dp[j] = 重さj以下でつくれる最大の価値
    for j in range(W+1):
        dp[j] = min(dp[j],dp[max(j-w,0)] + v)

print(dp[W])
