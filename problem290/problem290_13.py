from math import ceil
N,K = list(map(int, input().split()))
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort(reverse=True)
F.sort()
wk = 0
for i in range(N):
  wk += A[i] * F[i]
#print(wk)

def is_ok(arg):
  # 条件を満たすかどうか？問題ごとに定義
  cnt = 0
  for i in range(N):
    a,f = A[i], F[i]   
    if a*f <= arg:
      continue
    else:
      #(a-k) * f <= arg
      # a - arg/f <= k
      cnt += ceil(a-arg/f)
  return cnt <= K

def meguru_bisect(ng, ok):
  '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
  while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if is_ok(mid):
      ok = mid
    else:
      ng = mid
  return ok

ng = -1
ok = 10**12 + 10
ans = meguru_bisect(ng,ok)

print(ans)