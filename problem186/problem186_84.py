K, N = map(int, input().split())

A = list(map(int, input().split()))

c = abs(K - A[N-1] + A[0])

for i in range(N-1):
  d = abs(A[i] - A[i+1])
  if c < d:
    c = d
  else:
    c = c
    
print(K-c)