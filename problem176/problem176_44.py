n, k = map(int, input().split())
mod = 10 ** 9 + 7
dp = [0] * (k + 1)
ans = 0
for i in range(k, 0, -1):
    num = k // i
    dp[i] += pow(num, n, mod)

    for j in range(1, num):
        dp[i] -= dp[(j + 1) * i]
    ans += i * dp[i]
    ans %= mod
print(ans)
