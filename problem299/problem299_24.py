n=int(input())
A=list(map(int,input().split()))
r = [-1]*n
for i,a in enumerate(A):
  r[a-1]=i+1
for r2 in r:
  print(r2)