N=int(input())
A=list(map(int,input().split()))

mlt=0

for a in A:
  mlt^=a

for i in range(N):
  print(mlt^A[i],end=" ")