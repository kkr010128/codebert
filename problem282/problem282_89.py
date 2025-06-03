N,T = map(int, input().split())
data = [list(map(int, input().split())) for i in range(N)]
dp1 = [[0]*(N+1) for _ in range(T+1)]
dp2 = [[0]*(N+1) for _ in range(T+1)]

for t in range(T):
    for n in range(N):
        if t+1-data[n][0]>=0:
            dp1[t+1][n+1] = max(dp1[t+1][n],dp1[t+1-data[n][0]][n]+data[n][1])
            dp2[t+1][n+1] = max(dp2[t+1][n],dp2[t+1-data[n][0]][n]+data[n][1],
                                dp1[t][n]+data[n][1])
        else:
            dp1[t+1][n+1] = dp1[t+1][n]
            dp2[t+1][n+1] = max(dp2[t+1][n],dp1[t][n]+data[n][1])

print(dp2[T][N])
