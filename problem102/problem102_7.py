N,K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K+1,N+1):
  if A[i-K-1] < A[i-1]:
    print("Yes")
  else:
    print("No")