N = int(input())
A = list(map(int, input().split()))

# N日目の最大の所持金
dp = [1000] + [0] * (N-1)
for i in range(1, N):
    dp[i] = dp[i-1]

    for j in range(i):
        # j日に買える最大の株数
        max_unit = dp[j] // A[j]
        # その場合の所持金の変化
        money = dp[j] + (A[i]-A[j])*max_unit
        dp[i] = max(money, dp[i])

print(dp[-1])
