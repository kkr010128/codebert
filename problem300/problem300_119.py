from collections import defaultdict
from sys import stdin
input = stdin.readline


def prime_fatorization(n):
  # O(sqrt(n))
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
  A, B = list(map(int, input().split()))

  aprime = prime_fatorization(A)
  bprime = prime_fatorization(B)

  aset = set()
  bset = set()

  for ap in aprime.keys():
    aset.add(ap)

  for bp in bprime.keys():
    bset.add(bp)

  print(1+len(aset & bset))


if(__name__ == '__main__'):
  main()
