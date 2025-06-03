from decimal import Decimal
a,b,c = list(map(Decimal,input().split()))
d = Decimal('0.5')
A = a ** d
B = b ** d
C = c ** d
if A + B < C:
  print('Yes')
else:
  print('No')
