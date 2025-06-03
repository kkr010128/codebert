from decimal import *
getcontext().prec = 1000
a, b, c = map(lambda x: Decimal(x), input().split())

if a.sqrt() + b.sqrt() + Decimal('0.00000000000000000000000000000000000000000000000000000000000000000001') < c.sqrt():
    print('Yes')
else:
    print('No')

