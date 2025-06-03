def LI():
  return list(map(int,input().split()))
h,n=LI()

a=[]
b=[]
for _ in range(n):
  x,y=LI()
  a.append(x)
  b.append(y)
  
INF=10**15
dp=[INF]*(h+max(a)+10)
dp[0]=0
for i in range(0,h+1):
  for j,k in zip(a,b):
    dp[i+j]=min(dp[i+j],dp[i]+k)

ans=INF
for i in dp[h:]:
  ans=min(ans,i)
print(ans)