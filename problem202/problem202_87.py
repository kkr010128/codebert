n,a,b=map(int,input().split())
ans=0
m=n//(a+b)
l=n%(a+b)
ans+=m*a
if l<=a:
  print(ans+l)
else:
  print(ans+a)