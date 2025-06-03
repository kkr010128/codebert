from decimal import Decimal, getcontext
getcontext().prec = 50
a, b, c = map(Decimal, input().split())
half = Decimal("0.5")
if a**half + b**half < c**half:
    print("Yes")
else:
    print("No")