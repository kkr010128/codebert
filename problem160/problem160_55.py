N, M, Q = map(int, input().split())
a = [0 for _ in range(Q)]
b = [0 for _ in range(Q)]
c = [0 for _ in range(Q)]
d = [0 for _ in range(Q)]
for k in range(Q):
  a[k], b[k], c[k], d[k] = map(int, input().split())
A = [1 for _ in range(N)]

def point(A):
  p = 0
  for ai, bi, ci, di in zip(a, b, c, d):
    if A[bi-1] - A[ai-1] == ci:
      p += di
  return p

def next(A):
  k = 1
  while k < N+1:
    if A[-k] < M:
      A[-k] += 1
      return A
      break
    else:
      for j in range(1, k+1):
        A[-j] = A[-k-1] + 1
      k += 1

ans = point([M for _ in range(N)])
while A[0] < M:
  ans = max(ans, point(A))
  A = next(A)
print(ans)