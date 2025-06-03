a = [int(x) for x in input()[::-1]] + [0]
n = len(a)
dp = [[0] * 2 for _ in range(n)]
dp[0][0], dp[0][1] = a[0], 10-a[0]
for i in range(n-1):
    dp[i+1][0] = min(a[i+1]+dp[i][0], a[i+1]+dp[i][1]+1)
    dp[i+1][1] = min(10-a[i+1]+dp[i][0], 10-(a[i+1]+1)+dp[i][1])
print(min(dp[n-1]))
