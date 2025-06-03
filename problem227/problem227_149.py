n,k=map(int,input().split())
a=list(map(int,input().split()))

if n<=k:
  print(0)
  
else:
  a=sorted(a)
  b=n-k
  ans=0
  for x in range(n-k):
    ans+=a[x]
    
  print(ans)
