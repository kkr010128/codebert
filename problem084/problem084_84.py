N,M = [int(i) for i in input().split()]
A = list(range(N+1))
for _ in range(M):
  a,b = [int(i) for i in input().split()]
  while A[a] != a:
    a = A[a]
  while A[b] != b:
    b = A[b]
  a,b = [max(a,b),min(a,b)]
  A[a] = b
for i in range(N+1):
  n = A[i]
  while n != A[n]:
    n = A[n]
  A[i] = n
L = [0]*(N+1)
for a in A:
  L[a] += 1
print(max(L))