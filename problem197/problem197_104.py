a, b, c = map(int, input().split())
p = a**2 + b**2 + c**2 - 2*a*b - 2*b*c - 2*a*c
if p > 0 and c > a + b:
  print('Yes')
else:
  print('No')
