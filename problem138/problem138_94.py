import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n,s = na()
a = na()
mod = 998244353
dp = [0]*(s+1)
dp[0] = 1

for i in range(n):
    pd = [0]*(s+1)
    for j in range(s+1):
        if j+a[i] <= s:
            pd[j+a[i]] += dp[j]
        pd[j] += dp[j]*2%mod
    dp = pd

print(dp[s]%mod)