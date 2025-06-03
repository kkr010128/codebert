# coding: utf-8
import sys

def gcd(a, b):
    m = a % b
    if m == 0:
        return b
    return gcd(b, m)

for l in sys.stdin:
  x, y = map(int, l.split())
  g = gcd(x, y)
  l = x * y / g
  print g, l