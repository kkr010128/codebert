from decimal import *
from math import *
n,m=map(str,input().split())
p=Decimal(n)*Decimal(m)
print(floor(p))
