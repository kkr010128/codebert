import decimal


def multply(a: str, b: str) -> int:
    return int(decimal.Decimal(a) * decimal.Decimal(b))

a, b =  input().split()
print(multply(a, b))
