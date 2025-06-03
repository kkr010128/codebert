N = int(input())
A = list(map(int, input().split()))
S = sum(A)
ans = float("INF")
LS = [0]*(N+1)
LS[0] = 0
for i in range(N-1):
  LS[i+1] = A[i] + LS[i]
  ans = min(ans, abs(LS[i+1] - (S - LS[i+1])))
print(ans)