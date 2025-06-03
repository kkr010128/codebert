import math

def prime(x):
  p = {}
  last = math.floor(x ** 0.5)
  if x % 2 == 0:
    cnt = 1
    x //= 2
    while x & 1 == 0:
      x //= 2
      cnt += 1
    p[2] = cnt
  for i in range(3, last + 1, 2):
    if x % i == 0:
      x //= i
      cnt = 1
      while x % i == 0:
        cnt += 1
        x //= i
      p[i] = cnt
  if x != 1:
    p[x] = 1
  return p

N = int(input())

P = prime(N - 1)

if N == 2:
  print(1)
  exit()

ans = 1
for i in P.keys():
  ans *= P[i] + 1
ans -= 1

P = prime(N)
D = [1]
for i in P.keys():
  L = len(D)
  n = i
  for j in range(P[i]):
    for k in range(L):
      D.append(D[k] * n)
    n *= i


for i in D:
  if i == 1: continue
  t = N
  while (t / i == t // i):
    t //= i

  t -= 1
  if t / i == t // i:
    ans += 1

print(ans)
