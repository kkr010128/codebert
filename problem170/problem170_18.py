N,K=map(int,input().split())
ans=0
for i in range(K,N+2):
  if i!=(N+1):
    anssub=N*(N+1)//2 -(N-i)*(N-i+1)//2 - i*(i-1)//2+1
  else:
    anssub=1
  ans+=anssub
ans=ans%(10**9+7)
print(ans)