N, M = map(int, input().split())
f = 0
A = [-1 for i in range(N)]
for i in range(M):
  s, c = map(int, input().split())
  if A[s-1] != -1 and A[s-1] != c:
    print(-1)
    f = 1
    break
  A[s-1] = c
if f == 0:
  if N == 1 and (A[0] <= 0):
    print(0)
  elif N > 1 and A[0] == 0:
    print(-1)
  else:
    ans = 0
    for i in range(N):
      if i == 0:
        ans = ans * 10 + max(A[i], 1)
      else:
        ans = ans * 10 + max(A[i], 0)
    print(ans)