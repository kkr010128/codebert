n, m = map(int, input().split())
c = list(map(int, input().split()))
# dp[i][j] = i 番目までを使用して総和がj になる組み合わせ
INF = 5 * 10 ** 4
dp = [[INF] * (n + 1) for _ in range(m + 1)]
dp[0][0] = 0
for i in range(1, m + 1):
    for j in range(n + 1):
        if j >= c[i - 1]:
            dp[i][j] = min(
                dp[i - 1][j], dp[i - 1][j - c[i - 1]] + 1, dp[i][j - c[i - 1]] + 1
            )# dp[i - 1][j - c[i - 1]]　だと、複数回　コインを使う場合に対応していない 
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[m][n])


