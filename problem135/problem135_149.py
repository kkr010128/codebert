import decimal

a, b = input().split()
x, y = decimal.Decimal(a), decimal.Decimal(b)
print(int(x * y))