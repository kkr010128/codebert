N,T = map(int,input().split())
X = []
for i in range(N):
  a,b = map(int,input().split())
  X.append((a,b))
X.sort()
#print(X)
A = [];B = []
for i in range(N):
  A.append(X[i][0])
  B.append(X[i][1])
dp = [[0 for _ in range(T)] for _ in range(N+1)]
#dp[i][j] i番目までの料理を頼んだ時j分後の最大値
ans = 0
for i in range(N):
  time, aji = X[i]
  for j in range(T):
    if j-time >= 0:
      dp[i+1][j] = max(dp[i][j-time] + aji,dp[i][j])
    else:
      dp[i+1][j] = dp[i][j]
  
  if i < N-1:
    last = max(B[i+1:])
  else:
    last = 0
  #print(ans,last,dp[i+1][T-1])
  ans = max(ans,dp[i+1][T-1]+last)
print(ans)