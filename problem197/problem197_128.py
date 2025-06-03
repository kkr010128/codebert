from decimal import *
import math
 
getcontext().prec = 50
 
a, b, c = map(int, input().split())
a = Decimal(a)
b = Decimal(b)
c = Decimal(c)
 
a = Decimal.sqrt(a)
b = Decimal.sqrt(b)
c = Decimal.sqrt(c)
 
if a + b < c:
    print("Yes")
else:
    print("No")