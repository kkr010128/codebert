import sys

def gcd(x, y):
  if y == 1:
    return 1
  elif y == 0:
    return x
  else:
    return gcd(y, x % y)

line = sys.stdin.readline()
(a, b) = line.split()
a = int(a)
b = int(b)
if a > b:
  b, a = a, b

print gcd(a, b)