n = int(input())
a = [(int(x), i) for i, x in enumerate(input().split())]
a.sort(reverse=True)
aval, ai = zip(*a)
dp = [[0] * (n+1) for _ in range(n+1)]

for l in range(n):
    for r in range(n):
        if l + r >= n: break
        dp[l+1][r] = max(dp[l+1][r], dp[l][r] + aval[l+r] * abs(ai[l+r]-l))
        dp[l][r+1] = max(dp[l][r+1], dp[l][r] + aval[l+r] * abs(ai[l+r]-(n-r-1)))

print(max([dp[i][n-i] for i in range(n+1)]))
