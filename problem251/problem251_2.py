n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
dp = [[0]*n for _ in range(3)]
for i in range(n):
    if n < k:
        if t[i] == 'r':
            dp[2][i] = p
        elif t[i] == 's':
            dp[0][i] = r
        else:
            dp[1][i] = s
    else:
        if t[i] == 'r':
            dp[2][i] = max(dp[0][i-k], dp[1][i-k]) + p
            dp[0][i] = max(dp[1][i-k], dp[2][i-k])
            dp[1][i] = max(dp[0][i - k], dp[2][i - k])
        elif t[i] == 's':
            dp[0][i] = max(dp[1][i - k], dp[2][i - k]) + r
            dp[1][i] = max(dp[0][i - k], dp[2][i - k])
            dp[2][i] = max(dp[0][i - k], dp[1][i - k])
        else:
            dp[1][i] = max(dp[0][i - k], dp[2][i - k]) + s
            dp[0][i] = max(dp[1][i - k], dp[2][i - k])
            dp[2][i] = max(dp[0][i - k], dp[1][i - k])
res = 0
for i in reversed(range(n-k,n)):
    res += max(dp[0][i],dp[1][i],dp[2][i])
print(res)