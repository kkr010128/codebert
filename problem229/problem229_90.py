h,n=map(int,input().split())
a_=0
magic=[]
for i in range(n):
  a,b=map(int,input().split())
  a_=max(a,a_)
  c=[a,b]
  magic.append(c)
dp=[10**8+1]*(h+a_+1)
dp[0]=0
for i in range(n):
  a,b=magic[i]
  for j in range(len(dp)):
    if j+a<=h+a_:
      dp[j+a]=min(dp[j+a],dp[j]+b)
print(min(dp[h:]))     
