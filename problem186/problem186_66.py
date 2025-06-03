# -*= coding: utf-8 -*-
K, N = map(int, input().split())
A = list(map(int, input().split()))

d = [0] * N
for i in range(len(A)):
  if i == 0:
    d[0] = A[0] + (K - A[N-1]) if A[0] + (K - A[N-1]) <= A[N-1] else A[N-1]
    continue
  
  d[i] = A[i] - A[i-1]

d_max = max(d)

print(K - d_max)