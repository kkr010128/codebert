N=int(input())
A=list(map(int,input().split()))
h=0
for i in range(1,N):
  if A[i-1]<=A[i]:
    h+=0
  if A[i-1]>A[i]:
    h+=A[i-1]-A[i]
    A[i]=A[i-1]
print(h)