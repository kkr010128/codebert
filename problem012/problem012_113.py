N = int(input())
ns = [int(input()) for _ in range(N)]

#primes = set()
#def is_prime(n):
#  if n in primes:
#    return True
#
#  for m in range(2, n):
#    if is_prime(m) and n % m == 0:
#      return False
#
#  primes.add(n)
#  return True

# Proof:
# if n < d ^ 2 and n mod d = 0;
# n = ad (a in N)
# ad < d ^ 2
# a < d
# QED

def is_prime(n):
  if n < 2: return False
  if n == 2: return True
  if n % 2 == 0: return False

  d = 3
  while d ** 2 <= n:
    if n % d == 0:
      return False
    d += 2
  return True

print(len([n for n in ns if is_prime(n)]))