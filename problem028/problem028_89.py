N,M=list(map(int,input().split()))
C=list(map(int,input().split()))
dp=[0]+[50001 for _ in range(N)]


for i in range(M):
  for j in range(C[i],N+1):
    if C[i] > N:
      break
    elif dp[j-C[i]] != 50001:
      dp[j] = min(dp[j],dp[j-C[i]] + 1)

print(dp[N])
