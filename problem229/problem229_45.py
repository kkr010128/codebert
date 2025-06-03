h,n=map(int,input().split())
a=[]
b=[]
for i in range(n):
  aa,bb=map(int,input().split())
  a.append(aa)
  b.append(bb)
inf=10**10
f=h+max(a)+1
dp=[f*[inf]for _ in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
  dp[i]=dp[i-1]
  for j in range(f):
    if j+a[i-1]<f:
      dp[i][j+a[i-1]]=min(dp[i][j+a[i-1]],dp[i][j]+b[i-1])
  for j in range(f-1,0,-1):
    dp[i][j-1]=min(dp[i][j-1],dp[i][j])
print(dp[-1][h])
