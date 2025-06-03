import math
from functools import reduce
N = int(input())
A = list(map(int, input().split()))
a = set()

def gcd_list(numbers):
  return reduce(math.gcd, numbers)

def prime_factorize(n):
  global a
  tmp = []
  while n % 2 == 0:
    if 2 not in a:
      tmp.append(2)
      n //= 2
    else:
      return False
  f = 3
  while f * f <= n:
    if n % f == 0:
      if f not in a:
        tmp.append(f)
        n //= f
      else:
        return False
    else:
      f += 2
  if n != 1:
    if n not in a:
      tmp.append(n)
    else:
      return False
  a |= set(tmp)
  return True

flag = True
for i in range(N):
  ans = prime_factorize(A[i])
  if not ans:
    flag = False
    break
if flag:
  print('pairwise coprime')
elif gcd_list(A) == 1:
  print('setwise coprime')
else:
  print('not coprime')