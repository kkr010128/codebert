n,m=map(int,input().split())
A=list(map(int,input().split()))
ans=0
for i in range(n):
  if 4*m*A[i]<sum(A):
    continue
  else:
    ans+=1

if ans<m:
  print('No')
else:
  print('Yes')