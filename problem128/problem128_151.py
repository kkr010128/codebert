import math

X, N = map(int, input().split())
if N == 0:
  print(X)
else:
  p = list(map(int, input().split()))
  q = [int(i)-10 for i in range(121)]
  #print(q)

  for i in p:
    q.remove(i)

  ans = 0
  r0 = 100000
  for j in q:
    r = abs(j-X)
    if r0 > r:
      r0 = r
      ans = j
  print(ans)