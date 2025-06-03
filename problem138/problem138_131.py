import sys
input = sys.stdin.readline

mod = 998244353
N, S = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
dp = [0] * (S+1)
dp[0] = pow(2, N, mod)
two_inv = pow(2, mod-2, mod)
for i, a in enumerate(A):
    for j in range(a, S+1)[::-1]:
        dp[j] = (dp[j] + dp[j-a] * two_inv) % mod
print(dp[S])
