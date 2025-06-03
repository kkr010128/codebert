import sys

def gcd(a,b):
  if b == 0: return a
  else: return gcd(b,a%b)
  
for i in sys.stdin:
  a, b = map(int, i.split())
  g = gcd(a,b)
  print g, a/g*b