import sys
N, M = map(int, input().split())

A = [-1] * N

for i in range(M):
  s, c = map(int, input().split())
  if A[s-1] != c and A[s-1] != -1:
    print(-1)
    sys.exit()
  else:
    A[s-1] = c
  
if N >= 2 and A[0] == 0:
  print(-1)
  sys.exit()

res = 0

for i in range(N):
  if A[i] == -1:
    if i == 0 and N >= 2:
      A[i] = 1
    else:
      A[i] = 0
  res += A[i] * 10 ** (N-i-1)

print(res)