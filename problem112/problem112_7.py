N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7
plus = []
zero = []
minus = []
ans = 1

for k in range(N):
  if A[k] > 0:
    plus.append(A[k])
  elif A[k] < 0:
    minus.append(-1 * A[k])
  else:
    zero.append(A[k])
plus.sort(reverse = True)
minus.sort(reverse = True)
lp = len(plus)
lm = len(minus)
lz = len(zero)

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
        ans = ans * (-1) * minus[- k - 1] % mod  
      print(ans)
      exit()
  else:
    for k in range(K):
      ans = ans * (-1) * minus[k] % mod
    print(ans)
    exit()
elif lm == 0:
  for k in range(K):
    ans = ans * plus[k] % mod
  print(ans)
  exit()

p = 0
m = 0
for k in range(K):
  if plus[p] >= minus[m]:
    p += 1
    if p == lp:
      m = K - p  
      break
  else:
    m += 1
    if m == lm:
      p = K - m
      break

def main(mp, mm, plus, minus):
  mod = 10 ** 9 + 7
  ans = 1
  for k in range(mp):
    ans = ans * plus[k] % mod
  for k in range(mm):
    ans = ans * (-1) * minus[k] % mod
  print(ans)
  exit()

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