N,K,*A=map(int,open(0).read().split())
for _ in range(K):
  B=[0]*(N+1)
  for i,j in enumerate(A):
    B[max(0,i-j)]+=1
    B[min(N,i+j+1)]-=1
  for i in range(N):B[i+1]+=B[i]
  if A==B:break
  A=B
print(*A[:-1])