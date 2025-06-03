h, n = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

#dp[i][j] := i番目までの物でjの価値を実現するのに必要な最小コスト
dp = [[0] * (h+1) for _ in range(n+1)]
for j in range(1, h+1):
    dp[0][j] = float("inf")

for i in range(n):
    for j in range(h+1):
        if j < items[i][0]:
            dp[i+1][j] = min(dp[i][j], items[i][1])
        else:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j-items[i][0]] + items[i][1])

print(dp[n][h])