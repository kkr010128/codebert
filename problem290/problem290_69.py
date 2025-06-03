N, K = map(int, input().split())
A = sorted(map(int, input().split()))
F = sorted(map(int, input().split()), reverse=True)

ng = -1
ok = 0
for i in range(N):
  ok = max(A[i]*F[i], ok)

def is_ok(arg):
  cnt = 0
  for i in range(N):
    cnt += max(A[i] - arg//F[i], 0)
  return cnt <= K

def m_bisect(ng, ok):
  while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if is_ok(mid):
      ok = mid
    else:
      ng = mid
  return ok

print(m_bisect(ng, ok))