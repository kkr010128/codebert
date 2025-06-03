from decimal import Decimal

x = int(input())
cnt = 0

while True:
    a = cnt ** 5
    if a < x:
        a = x - a
        z = -1
    else:
        a -= x
        z = 1

    a = Decimal(a) ** Decimal("0.2")
    if a % 1 == 0:
        print(cnt, int(a * z))
        break

    cnt += 1