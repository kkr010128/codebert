from decimal import Decimal
a,b,c = map(int,input().split())
a = Decimal(a)
b = Decimal(b)
c = Decimal(c)
if Decimal.sqrt(a) + Decimal.sqrt(b) < Decimal.sqrt(c):
    print('Yes')
else:
    print('No')