import sys

N, K = (int(x) for x in input().split())
H = list(map(int, input().split()))
ans=0

if K>=N:
  print(0)
  sys.exit(0)
  
H.sort(reverse=True)
del H[0:K]
for i in range(len(H)):
  ans+=H[i]
print(ans)