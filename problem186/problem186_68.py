K, N = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.append(A[0]+K)
res = []
for i in range(N):
  res.append(abs(A[i]-A[i+1]))
print(K - max(res))