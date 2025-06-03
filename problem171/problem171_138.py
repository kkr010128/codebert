import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
iA = [(i, A[i]) for i in range(N)]
iA.sort(key=lambda t: t[1], reverse=True)
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if i+j<N:
            idx, v = iA[i+j]
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+v*abs(idx-i))
            dp[i][j+1] = max(dp[i][j+1], dp[i][j]+v*abs(N-1-j-idx))

ans = 0

for i in range(N+1):
    ans = max(ans, dp[i][N-i])

print(ans)