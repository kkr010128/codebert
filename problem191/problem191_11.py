from decimal import Decimal

L = int(input())

w = Decimal(L / 3)
d = Decimal(L / 3)
h = Decimal(L / 3)

ans = Decimal(w * d * h)

print(ans)