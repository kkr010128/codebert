n,a,b=map(int,input().split())

rep=n//(a+b)
rep2=n%(a+b)
ans=rep*a
if rep2>=a:
  ans+=a
  print(ans)
else:
  ans+=rep2
  print(ans)
