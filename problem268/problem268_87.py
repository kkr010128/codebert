import sys
input=lambda: sys.stdin.readline().rstrip()

n=int(input())
A=[int(i) for i in input().split()]
ans=1
mod=10**9+7
C=[0,0,0]
for i in range(n):
  cur=A[i]
  ct=0
  Chk=True
  for i,c in enumerate(C):
    if cur==c:
      ct+=1
      if Chk:
        C[i]+=1
        Chk=False
  ans=(ans*ct)%mod
  
print(ans)
