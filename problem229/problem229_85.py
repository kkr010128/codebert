H, N = map(int, input().split())
A = []
max_A = 0
for i in range(N):
    A.append(tuple(map(int, input().split())))
    max_A = max(max_A, A[i][0])

INF = 10**9
dp = [INF] * (2 * 10 ** 4 + 1)
dp[0] = 0

for i in range(2 * 10 ** 4):
    for a, b in A:
        if i + a <= 2 * 10 ** 4:
            dp[i+a] = min(dp[i]+b, dp[i+a])

print(min(dp[H:]))