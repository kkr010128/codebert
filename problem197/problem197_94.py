from decimal import Decimal
a,b,c=map(lambda x:Decimal(x)**Decimal("0.5"),input().split())
print("Yes" if a+b<c else "No")