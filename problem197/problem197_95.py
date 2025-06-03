import math

a, b, c = [int(n) for n in input().split()]

if 4*a*b < (c - a - b) ** 2 and c > a + b:
  print('Yes')
else:
  print('No')