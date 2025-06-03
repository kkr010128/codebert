import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0]*(N+1)
dp[0] = 1000

for i in range(1, N+1):
    dp[i] = dp[i-1]
    
    for j in range(i):
        dp[i] = max(dp[i], dp[j]//A[j]*A[i-1]+dp[j]%A[j])

print(dp[N])