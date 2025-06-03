from decimal import Decimal
A,B,C=map(str,input().split())
if Decimal(A)**Decimal("0.5")+Decimal(B)**Decimal("0.5")<Decimal(C)**Decimal("0.5"):
    print("Yes")
else:
    print("No")
