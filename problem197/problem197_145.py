from decimal import Decimal
a,b,c = map(int,input().split())
a = Decimal(a) ** Decimal(0.5)
b = Decimal(b) ** Decimal(0.5)
c = Decimal(c) ** Decimal(0.5)
if Decimal(a) + Decimal(b) < Decimal(c):
    print('Yes')
else:
    print('No')