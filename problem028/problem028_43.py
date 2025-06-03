n, m = map(int, input().split())
C = sorted(tuple(map(int, input().split())))

dp = list(range(0, n+1))
for i in range(m):
    c = C[i]
    ndp = [50000] * (n+1)
    for j in range(n+1):
        if j < c:
            ndp[j] = dp[j]
        else:
            ndp[j] = min(dp[j], ndp[j-c] + 1)
    dp = ndp
print(ndp[-1])

