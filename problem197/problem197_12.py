import decimal

a, b, c = map(str, input().split())

sqrta = decimal.Decimal(a).sqrt()
sqrtb = decimal.Decimal(b).sqrt()
sqrtc = decimal.Decimal(c).sqrt()

if sqrta + sqrtb < sqrtc:
    print("Yes")
else:
    print("No")