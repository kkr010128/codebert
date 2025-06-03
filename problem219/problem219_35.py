nl = list(input())


# 繰り上げと繰り下げ
dp = [[0, 10000] for i in range(len(nl) + 1)]

for i, n in enumerate(nl[::-1]):
    n = int(n)
    dp[i+1][0] = min(dp[i][0] + n, dp[i][1] + n + 1)
    dp[i+1][1] = min(10 - n + dp[i][0], 10 - n - 1 + dp[i][1])



print(min(dp[-1][0], dp[-1][1]+1))



