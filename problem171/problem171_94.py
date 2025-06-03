import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))

L = list(range(N))
L.sort(key = lambda x: A[x], reverse = True)

dp = [[0]*(N+1) for _ in range(N+1)]

for s in range(N):
    l = L[s]
    a = A[l]
    for i in range(s+1):
        j = s-i
        dp[i+1][j] = max(dp[i+1][j], dp[i][j]+a*abs(l-i))
        dp[i][j+1] = max(dp[i][j+1], dp[i][j]+a*abs(l-(N-s+i-1)))
ans = 0
for i in range(N+1):
    ans = max(ans, dp[i][N-i])
print(ans)