import itertools as it
N=int(input())
W=list(range(1,N+1))
c1=-1
c2=-1
c=0
L=tuple(map(int,input().split()))
M=tuple(map(int,input().split()))
if L==M:
  print(0)
  exit()
for i in it.permutations(W,N):
  c+=1
  if i==L:
    c1=c
  elif i==M:
    c2=c
print(abs(c1-c2))