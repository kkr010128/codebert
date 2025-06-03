import math

H, N = list(map(int, input().split()))
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = list(map(int, input().split()))

dp = [0]*(H+1)

dp[0] = 0

for i in range(1,H+1):
    dp_min = math.inf
    for j in range(N):
        dp_min = min(dp_min, dp[max(0,i-A[j])] + B[j])
    dp[i] = dp_min

print(dp[H])