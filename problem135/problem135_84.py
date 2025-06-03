from decimal import *
import math

A, B = input().split()
a = Decimal(A)
b = Decimal(B)
ib = Decimal(100*b)

print(math.floor((a*ib)/Decimal(100)))