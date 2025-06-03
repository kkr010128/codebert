import sys
input=lambda: sys.stdin.readline().rstrip()
n,k=map(int,input().split())
mod=10**9+7
A=[0]*(k+1)
for i in range(1,k+1)[::-1]:
  cur=pow(k//i,n,mod)
  for j in range(2,k+1):
    if i*j>k:
      break
    else:
      cur-=A[i*j]
  A[i]=cur
ans=0
for i in range(1,k+1):
  ans=(ans+i*A[i])%mod
print(ans)
