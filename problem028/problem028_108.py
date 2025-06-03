length, t = map(int, input().split(" "))
target = [int(n) for n in input().split(" ")]
dp = [float("inf") for n in range(length + 1)]
dp[0] = 0
for i, coin in enumerate(target):
    for j in range(length):
        if coin + j <= length:
            dp[coin + j] = min(dp[coin + j], dp[j] + 1)
print(dp[length])
