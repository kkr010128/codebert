import sys

ans=0
A, B, C, K = (int(x) for x in input().split())

if A>K:
  print(K)
  sys.exit(0)
else:
  K-=A
  ans+=A
  
if B>K:
  print(ans)
  sys.exit(0)
else:K-=B

if C>K:
  print(ans-K)
  sys.exit()
else:
  ans-=C
  print(ans)