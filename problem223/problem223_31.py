n,k=map(int,input().split())
p=[0]+list(map(int,input().split()))
for i in range(n+1):
  p[i]=(p[i]+1)/2
for i in range(n):
  p[i+1]+=p[i]
ans=0
for i in range(n-k+1):
  ans=max(ans,p[i+k]-p[i])
print(ans)