ans=-10**18
a,b,c,d=map(int,input().split())
if a<=0<=b or c<=0<=d:
  ans=0
ans=max(ans,a*c,a*d,b*c,b*d)
print(ans)