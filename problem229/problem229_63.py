import heapq
H, N = map(int, input().split())
A = [] #W
B = [] #V
for i in range(N):
    ai, bi = map(int, input().split())
    A += [ai]
    B += [bi]
maxA = max(A)
dp = [[0 for j in range(H+maxA+1)]for i in range(N+1)]

for j in range(1, H+maxA+1):
    dp[0][j] = float('inf')

for i in range(N):
    for j in range(H+maxA+1):
        if j - A[i] < 0:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j-A[i]] + B[i])
ans = float('inf')
for j in range(H, H+maxA+1):
    ans = min(ans, dp[N][j])
print(ans)