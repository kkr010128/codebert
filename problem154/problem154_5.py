N,K=list(map(int, input().split()))
A=[0]*(N+1)
for _ in range(K):
  k=int(input())
  a=list(map(int, input().split()))
  for i in a:
    A[i]+=1
c=0
for i in range(1,N+1):
  c+=not A[i]
print(c)