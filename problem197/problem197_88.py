from decimal import Decimal
a,b,c = input().split()
if Decimal(a).sqrt()+Decimal(b).sqrt()<Decimal(c).sqrt():
    print('Yes')
else:
    print('No')
