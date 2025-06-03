# C Traveling Salesman around Lake

K, N = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
before = A[0]
for i in range(1, len(A)):
  ans = max(ans, A[i] - before)
  before = A[i]
  
ans = max(ans, A[0] + K - A[N-1])

print(K - ans)