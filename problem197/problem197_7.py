import math
from decimal import Decimal, getcontext
a,b,c = map(int, input().split())

t = c-a-b

if t <= 0:
    print('No')
    exit()

if 4*a*b < t*t:
    print('Yes')
else:
    print('No')