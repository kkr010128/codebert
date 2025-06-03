

import decimal
#decimal.getcontext().prec = 30
a,b,c = list(map(int, input().split()))
a = decimal.Decimal(a)
b = decimal.Decimal(b)
c = decimal.Decimal(c)
d = decimal.Decimal(0.5)
e = decimal.Decimal(1/10000000)

#print(a**decimal.Decimal(0.5))

if(a**d + b**d < (c)**d ):
    print("Yes")
else:
    print("No")
#print(a**d + b**d , (c)**d)
