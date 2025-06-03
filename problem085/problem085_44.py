N=int(input())
A=list(map(int,input().split()))
import math
a=A[0]
for i in range(1,N):
  a=math.gcd(a,A[i])
def f():
  a=A[0]
  for i in range(1,N):
    a=math.gcd(a,A[i])
  if a==1:
    print("setwise coprime")
    exit()
  else:
    print("not coprime")
    exit()
  
D=[0]*(10**6+1)
for i in range(2,10**6+1):
  for j in range(2*i,10**6+1,i):
    if D[j]==0:
      D[j]=i
for i in range(10**6+1):
  if D[i]==0:
    D[i]=i

s=set()
import copy
for i in range(N):
  tmp=set()
  k=A[i]
  while k>1:
    tmp.add(D[k])
    k=k//D[k]
  for i in tmp:
    if i in s:
      f()
    else:
      s.add(i)


print("pairwise coprime")
