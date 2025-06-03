n = int(input())
dp = [0] * (n + 1)
for x in range(1, n + 1):
    for y in range(x, n + 1, x):
        dp[y] += 1
print(sum(dp[1:n]))