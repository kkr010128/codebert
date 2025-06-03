N, *A = map(int, open(0).read().split())
A.sort()
dp = [True]*3*int(1e6)
x = -1
for a in A:
  if a == -1: continue
  x = a
  while x <= A[-1]:
    x += a
    dp[x] = False
  x = a

res = 0
for i, a in enumerate(A):
  if i > 0 and a == A[i-1]: continue
  if i < N-1 and a == A[i+1]: continue
  if dp[a]: res += 1
print(res)