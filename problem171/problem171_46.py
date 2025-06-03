N = int(input())
A = list(map(int, input().split()))

B = sorted(A, reverse=True)

C = [0] * N

i = 0
while(1):
    if i >= N:
        break
    for j in range(N):
        if A[j] == B[i]:
            C[i] = j
            if i != N-1 and B[i] == B[i+1]:
                i += 1
    i += 1

dp = [[0] * (N+1) for i in range(N+1)]
for i in range(N+1):
    for j in range(i+1):
        if j > 0 and i-j > 0:
            dp[j][i-j] = max([dp[j-1][i-j] + B[i-1] * abs(C[i-1] - (j-1)), dp[j][i-j-1] + B[i-1] * abs(C[i-1] - (N-1-(i-j-1)))])
        elif j == 0 and i-j > 0:
            dp[j][i-j] = dp[j][i-j-1] + B[i-1] * abs(C[i-1] - (N-1-(i-j-1)))
        elif i-j == 0 and j > 0:
            dp[j][i-j] = dp[j-1][i-j] + B[i-1] * abs(C[i-1] - (j-1))


ans = 0
for i in range(N+1):
    ans = max([ans, dp[i][N-i]])

print(ans)