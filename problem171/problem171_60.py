import sys
input = sys.stdin.readline

N = int(input())
A = list(zip(list(map(int, input().split())), range(N)))
A.sort(reverse=True)
dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    a, k = A[i-1]
    dp[i][0] = dp[i-1][0] + a * abs(N-i-k)
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j] + a * abs(N-(i-j)-k), dp[i-1][j-1] + a * abs(j-1-k))
    dp[i][i] = dp[i-1][i-1] + a * abs(i-1-k)
print(max(dp[N]))