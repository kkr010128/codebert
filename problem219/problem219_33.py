N = input()[::-1]
L = len(N)
dp = [[0]*2 for _ in range(L+1)]
dp[0][1] = 10**18

for i in range(L):
    n = int(N[i])
    dp[i+1][0] = min(dp[i][0]+n, dp[i][1]+n+1)
    dp[i+1][1] = min(dp[i][0]+10-n, dp[i][1]+10-n-1)

print(min(dp[L][0], dp[L][1]+1))