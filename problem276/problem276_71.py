N = int(input())
A = list(map(int,input().split()))
c = sum(A)/2

S = [0] * (N+1)
S[0] = 0
for i in range(N):
  S[i+1] = A[i] + S[i]

m = float("INF")
j = -1
for i in range(1, N+1):
  if abs(c - S[i]) < m:
    m = abs(c - S[i])
    j = i

print(abs((S[N] - S[j]) - S[j]))