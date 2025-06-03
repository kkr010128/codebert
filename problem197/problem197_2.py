from decimal import *
getcontext().prec=1000
a,b,c=map(int,input().split())
A=Decimal(a)**Decimal("0.5")
B=Decimal(b)**Decimal("0.5")
C=Decimal(c)**Decimal("0.5")
D= Decimal(10) ** (-100)
if A+B+D<C:
    print("Yes")
else:
    print("No")