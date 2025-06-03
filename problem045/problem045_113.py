from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
inp = input()
a = inp.split()
b = int(a[0])//int(a[1])
c = int(a[0])%int(a[1])
d = Decimal(a[0])/Decimal(a[1])
d = d.quantize(Decimal('0.000001'),rounding=ROUND_HALF_UP)
print(b,c,d)
