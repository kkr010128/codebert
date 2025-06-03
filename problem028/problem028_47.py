n,m = map(int,input().split())
c = list(map(int,input().split()))

c.sort(reverse = True)

dp = [[float('inf') for i in range(n+1)] for j in range(m+1)]

for j in range(m+1):
    dp[j][0] = 0

for j in range(1,m+1):
    for i in range(c[j-1],n+1):
        dp[j][i] = min(dp[j-1][i], dp[j][i-c[j-1]] + 1)

print(dp[m][n])