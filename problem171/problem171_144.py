N = int(input())
A = list(map(int,input().split()))
B = [i for i in range(1,N+1)]
C = zip(A, B)
C = sorted(C, reverse = True)
A, B = zip(*C)
dp = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(N):
    for j in range(i + 2):
        if j == 0:
            dp[0][i-j+1] = dp[0][i-j] + A[i] * (N - (i - j) - B[i])
        elif j == i+1:
            dp[j][0] = dp[j-1][0] + A[i] * (B[i] - j)
        else:
            dp[j][i-j+1] = max(dp[j][i-j] + A[i] * (N - (i - j) - B[i]), dp[j-1][i-j+1] + A[i] * (B[i] - j))
ans = 0
for i in range(N+1):
    ans = max(ans, dp[i][N-i])
print(ans)