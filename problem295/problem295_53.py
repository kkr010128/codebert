import sys


INF = 1 << 32 - 1
S = sys.stdin.readlines()
N, M, L = map(int, S[0].split())

dp = [[INF] * N for _ in range(N)]

for i in range(1, M + 1):
    A, B, C = map(int, S[i].split())
    dp[A - 1][B - 1] = C
    dp[B - 1][A - 1] = C
for i in range(N):
    dp[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


dp2 = [[INF] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if dp[i][j] <= L:
            dp2[i][j] = 1
for i in range(N):
    dp2[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp2[i][j] = min(dp2[i][j], dp2[i][k] + dp2[k][j])


Q = int(S[M + 1])
for i in range(M + 2, M + 2 + Q):
    s, t = map(int, S[i].split())
    refuel = dp2[s - 1][t - 1]
    if refuel >= 10 ** 3:
        print(-1)
    else:
        print(refuel - 1)
