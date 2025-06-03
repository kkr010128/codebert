N=int(input())
A=list(map(int,input().split()))
res=[0]*N
for i in range(N):
  res[A[i]-1]=i+1
for j in res:
  print(j,end=" ")