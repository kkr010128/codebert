n, m = map(int, input().split())
*C, = map(int, input().split())

dp = [n]*(n+1)
dp[0] = 0

for c in C:
    for i in range(n+1):
        if i+c > n:
            break
        dp[i+c] = min(dp[i+c], dp[i] + 1)

print(dp[n])
