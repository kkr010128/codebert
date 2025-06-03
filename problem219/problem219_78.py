N = input()
L = len(N)

# dp[i][j]: 紙幣の最小枚数
# i: 決定した桁数
# j: 1枚多めに渡すフラグ
dp = [[float("inf")] * 2 for _ in range(L + 1)]

# 初期条件
dp[0][0] = 0
dp[0][1] = 1

# 貰うDP
for i in range(L):
    n = int(N[i])

    dp[i + 1][0] = min(dp[i][0] + n, dp[i][1] + (10 - n))
    dp[i + 1][1] = min(dp[i][0] + (n + 1), dp[i][1] + (10 - (n + 1)))

print(dp[L][0])