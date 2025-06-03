N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A, reverse = True)
for i in range(min(K, N)):
  A[i] = 0
ans = sum(A)
print(ans)