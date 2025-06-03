INF = 2**60 # 無限大を表す値
H, N = map(int, input().split())
AB = [map(int, input().split()) for i in range(N)]
dp = [[INF] * (H + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i, (A, B) in enumerate(AB):
    for j in range(H+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i+1][j] = min(dp[i+1][j], dp[i+1][max(j-A, 0)] + B)
print(dp[N][H])