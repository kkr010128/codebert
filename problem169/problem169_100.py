n=int(input())
a=list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(n-1):
  dp[a[i]]+=1
for i in range(n):
  print(dp[i+1])