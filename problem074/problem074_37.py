n, k = map(int, input().split())

d = [[], []]
for _ in range(k):
    l, r = map(int, input().split())
    d[0].append(l-1)
    d[1].append(r-1)

dp = [0]*n
dp[0] = 1
a = [0]*(n+1)
a[1] = dp[0]
for i in range(1, n):
    for j in range(k):
        r = i - d[0][j]
        l = i - d[1][j]
        if l < 1:
            l = 1
        if r < 0:
            continue
        dp[i] += a[r] - a[l-1]
        dp[i] %= 998244353
    a[i+1] = (a[i] + dp[i]) % 998244353
print(dp[-1])
