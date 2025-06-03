from decimal import Decimal
import math

a, b, x = list(map(Decimal, input().split()))

if a * a * b > 2 * x:
    tri = x / a
    c = tri * Decimal(2) / b
    d = (c ** 2 + b ** 2) ** Decimal("0.5")
    cos_a = (b ** 2 + d ** 2 - c ** 2) / (2*b*d)
    print(90 - math.degrees(math.acos(cos_a)))
else:
    tri = (a * a * b - x) / a
    e = tri * Decimal(2) / a
    f = (a ** 2 + e ** 2) ** Decimal("0.5")
    cos_e = (f ** 2 + a ** 2 - e ** 2) / (2*f*a)
    print(math.degrees(math.acos(cos_e)))
#print(cosin)
