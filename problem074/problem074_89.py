n, k = list(map(int, input().split()))
s = []
for i in range(k):
    a, b = list(map(int, input().split()))
    s.append((a, b))
dp = [0]*(n+1)
v = 0
mod = 998244353
for i in range(1, n+1):
    if i == 1:
        for l, r in s:
            if i+l <= n:
                dp[i+l] += 1
            if i+r+1 <= n:
                dp[i+r+1] -= 1
    else:
        v += dp[i]
        v %= mod
        for l, r in s:
            if i+l <= n:
                dp[i+l] += v
            if i+r+1 <= n:
                dp[i+r+1] -= v


print(v % mod)
