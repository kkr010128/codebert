N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 1000000007
plus = []
minus = []
ans = 1
lp = 0
lm = 0
lz = 0
for k in range(N):
  if A[k] > 0:
    plus.append(A[k])
    lp += 1
  elif A[k] < 0:
    minus.append(A[k])
    lm += 1
  else:
    lz += 1
plus.sort(reverse = True)
minus.sort()
def main(mp, mm, plus, minus):
  mod = 1000000007
  ans = 1
  for k in range(mp):
    ans = ans * plus[k] % mod
  for k in range(mm):
    ans = ans * minus[k] % mod
  print(ans)
  exit()
if lz + K > N:
  print(0)
  exit()
elif lp == 0: 
  if K % 2 == 1:
    if lz > 0:
      print(0)
      exit()
    else:
      for k in range(K):
        ans = ans * minus[- k - 1] % mod
      print(ans)
      exit()
  else:
    main(0, K, plus, minus)
elif lm == 0:
  main(K, 0, plus, minus)
p = 0
m = 0
for _ in range(K):
  if plus[p] >= -1 * minus[m]:
    p += 1
    if p == lp:
      m = K - p
      break
  else:
    m += 1
    if m == lm:
      p = K - m
      break
if m % 2 == 0:
  main(p, m, plus, minus)
else:
  if p == lp:
    if m != lm:
      main(p - 1, m + 1, plus, minus)
    else:
      if lz > 0:
        print(0)
        exit()
      else:
        main(p, m, plus, minus)
  elif m == lm:
    main(p + 1, m - 1, plus, minus)
  elif p == 0:
    main(p + 1, m - 1, plus, minus)
  else:
    if plus[p] * plus[p - 1] > minus[m - 1] * minus[m]:
      main(p + 1, m - 1, plus, minus)
    else:
      main(p - 1, m + 1, plus, minus)