H, N = map(int, input().split())
AB = []
for _ in range(N):
    A, B = map(int, input().split())
    AB.append([A, B])
AB = sorted(AB, key=lambda x:x[0], reverse=True)
INF = float("inf")
dp = [INF for _ in range(H+1)]
dp[0] = 0

# DP
for i in range(1, H+1):
    for a, b in AB:
        if a >= i:
            dp[i] = min(dp[i], b)
            continue
        else:
            dp[i] = min(dp[i], dp[i-a]+b)
print(dp[-1])