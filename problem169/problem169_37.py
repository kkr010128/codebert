N=int(input())
A=list(map(int,input().split()))
B=[0]*N
for x in range(N-1):
  B[A[x]-1] += 1
for y in range(N):
  print(B[y])