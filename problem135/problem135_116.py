from decimal import *
getcontext().prec = 29
a,b=map(Decimal,input().split())
print(int(a*b))
