n=int(input())
A=[{} for _ in range(n)]
for i in range(n):
  for _ in range(int(input())):
    x,y=map(int,input().split())
    A[i][x]=y
a=0
for i in range(2**n):
  t=0
  for j in range(n):
    if i>>j&1:
      if A[j] and any(i>>~-k&1!=A[j][k] for k in A[j]): break
      else: t+=1
  else: a=max(a,t)
print(a)