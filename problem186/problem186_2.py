K, N = map(int, input().split())
A = list(map(int, input().split()))
res = A[0] + (K - A[N-1])
for i in range(1, N):
  dist = A[i] - A[i-1]
  if res < dist:
    res = dist
print(K - res)