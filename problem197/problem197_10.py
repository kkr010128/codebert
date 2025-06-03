from decimal import *
x,y,z = map(int,input().split())
a=Decimal(x)
b=Decimal(y)
c=Decimal(z)
if Decimal((c-a-b)**Decimal(2)) > Decimal(Decimal(4)*a*b) and c-a-b > 0:
    print('Yes')
else:
    print('No')