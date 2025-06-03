N, T = map(int, input().split())

A, B = zip(*[tuple(map(int, input().split())) for _ in range(N)])
dp1 = [[0]*(T) for _ in range(N+1)]
dp2 = [[0]*(T) for _ in range(N+2)]

for i in range(N):
    for j in range(T):
        dp1[i+1][j] = max(dp1[i][j], dp1[i][j-A[i]]+B[i]) if j-A[i]>=0 else dp1[i][j]

for i in range(N, 0, -1):
    for j in range(T):
        dp2[i][j] = max(dp2[i+1][j], dp2[i+1][j-A[i-1]]+B[i-1]) if j-A[i-1]>=0 else dp2[i+1][j]

ans = -1
for i in range(1, N+1):
    for j in range(T):
        ans = max(ans, dp1[i-1][j]+dp2[i+1][T-j-1]+B[i-1])

print(ans)