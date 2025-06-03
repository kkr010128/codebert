import sys


def gcd(m, n):
  if n > m:
    m, n = n, m
  if n == 0:
    return m
  else:
    return gcd(n, m % n)


for line in sys.stdin:
  try:
    a, b = [int(i) for i in line.split()]
    g = gcd(a, b)
    l = a * b / g
    print("%d %d" % (g, l))
  except:
    break