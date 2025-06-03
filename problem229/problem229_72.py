h,n=map(int,input().split())
a=[]
b=[]
for _ in range(n):
  x,y=map(int,input().split())
  a.append(x)
  b.append(y)
a_=max(a)
dp=[10**8]*(h+1+a_)
dp[0]=0
for i in range(1,len(dp)):
  for j in range(n):
    if 0<=i-a[j]<=len(dp)-1-a[j]:
      dp[i]=min(dp[i],dp[i-a[j]]+b[j])
print(min(dp[h:]))