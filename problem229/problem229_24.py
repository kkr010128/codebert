H,N = map(int,input().split());INF = float("inf")
A=[];B=[]
for i in range(N):
  a,b = map(int,input().split())
  A.append(a);B.append(b)
#print(A,B)

dp = [INF for _ in range(H+1)] #dp[i] HPがi残っているときの、魔力の消費最小
dp[H] = 0
for i in reversed(range(H+1)):
  #print(i)
  #print(dp)
  for j in range(N):
    if i - A[j] >= 0:
      dp[i-A[j]] = min(dp[i-A[j]], dp[i] + B[j])
    else:
      dp[0] = min(dp[0], dp[i] + B[j])
ans = dp[0]
print(ans)