


N,M = map(int, input().split())
C = list(map(int, input().split()))

C.sort()
dp = [[float("inf") for _ in range(N+1)] for _ in range(M+1)]
dp[0][0] = 0


#i番目までのコインを使えるときに、j円を作る場合の、コインの最小枚数を求める
for i in range(M):
    for j in range(N+1):
        # i番目を使えない場合
        if C[i] > j:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j - C[i]] + 1)

print(dp[-1][-1])
