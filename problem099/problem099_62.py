from math import ceil

n, k = map(int, input().split())
logs = list(map(int, input().split()))


def is_ok(num):
  t = 0
  for log in logs:
    if log <= num:
      continue
    t += ceil(log / num) - 1
  return t <= k

ng = 0
ok = 10 ** 9

while ok - ng > 1 :
  m = (ok + ng) // 2
  
  if is_ok(m):
    ok = m
  else:
    ng = m

print(ceil(ok))