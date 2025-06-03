from fractions import Decimal

a,b,c=map(int,input().split())

if a+b+2*(a*b)**Decimal('0.5') < c:
  print('Yes')
else:
  print('No')