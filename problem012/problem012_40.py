
N=int(raw_input())
s=[int(raw_input()) for x in range(N)]


def is_prime(n):
  i = 2
  while i * i <=n:
    if n % i == 0:
      return False
    i += 1
  return True

a=filter(is_prime,s)
print len(a)