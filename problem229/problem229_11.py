H, N = list(map(int, input().split()))
A = [[0]*2 for _ in range(N)]
for _ in range(N):
    A[_][0], A[_][1] = list(map(int, input().split()))
# print(A)
# A.sort(key=lambda x: x[1])

INF = float('inf')
dp = [INF]*(H+1)
dp[0] = 0

for i in range(H):
    if dp[i] == INF:
        continue
    for j in range(N):
        a = A[j][0]
        b = A[j][1]
        if i+a >= H:
            dp[H] = min(dp[H], dp[i]+b)
        else:
            dp[i+a] = min(dp[i+a], dp[i]+b)
print(dp[H])