H, N = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

dp = [10 ** 18] * (H + 1)

dp[0] = 0

for i in range(H + 1):
    for A, B in AB:
        if i + A >= H:
            dp[H] = min(dp[H], dp[i] + B)
        else:
            dp[i + A] = min(dp[i + A], dp[i] + B)

res = dp[H]

print(res)
