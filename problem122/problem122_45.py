import collections

N=int(input())
A=list(map(int,input().split()))
X=collections.Counter(A)
Q=int(input())

ans=sum(A)
for i in range(Q):
  B,C=map(int,input().split())
  ans+=(C-B)*X[B]
  print(ans)
  X[C]+=X[B]
  X[B]=0
