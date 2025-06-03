N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

At = [0]*(N+1)
Bt = [0]*(M+1)

for i in range(N):
  At[i+1] = At[i] + A[i]
for i in range(M):
  Bt[i+1] = Bt[i] + B[i]

j = M
ans = 0
for i in range(N+1):
  if At[i] > K:
    break
  while At[i] + Bt[j] > K:
    j = j - 1
  if ans < i + j:
  	ans = i+j 

print(ans)