from decimal import Decimal

a, b, c = map(int, input().split())

if a + b < c - (2*(Decimal(a*b).sqrt())):
    print("Yes")
else:
    print("No")
