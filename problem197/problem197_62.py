from decimal import Decimal
from math import sqrt
a, b, c = map(int, input().split())
print('Yes' if Decimal(a).sqrt()+Decimal(b).sqrt() < Decimal(c).sqrt() else 'No')
