import math
from sys import stdin
input = stdin.readline


def prime_fatorization(n):
  # O(sqrt(n))
  from collections import defaultdict
  # a = []
  a = defaultdict(int)
  while not(n % 2):
    # a.append(2)
    a[2] += 1
    n //= 2
  f = 3
  while f * f <= n:
    if not(n % f):
      # a.append(f)
      a[f] += 1
      n //= f
    else:
      f += 2
  if n != 1:
    # a.append(n)
    a[n] += 1
  return a


def main():
  N, M = list(map(int, input().split()))
  A = list(map(lambda x: int(x)//2, input().split()))

  pre = A[0]

  for i in range(1, N):
    if pre % 2 != A[i] % 2:
      print(0)
      return

  if not A[0] % 2:
    fac2 = prime_fatorization(A[0])[2]
    for i in range(1, N):
      if not A[i]//(2**fac2) % 2:
        print(0)
        return

  lcm = A[0]
  for i in range(1, N):
    lcm = lcm * A[i] // math.gcd(lcm, A[i])
  print((M // lcm + 1) // 2)


if(__name__ == '__main__'):
  main()
