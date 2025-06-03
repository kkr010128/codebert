from decimal import Decimal
a,b,c=map(Decimal,input().split())
root=Decimal("0.5")
print("Yes" if a**root+b**root<c**root else "No")