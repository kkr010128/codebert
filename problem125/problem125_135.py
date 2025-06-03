n = int(input())


def gcd(a,b):
  if b == 0:
    return a
  return gcd(b, a%b)


print((360 * n // gcd(360, n)) // n)