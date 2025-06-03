from decimal import Decimal, ROUND_HALF_UP

l = int(input())

ans = Decimal(str((l/3)**3)).quantize(Decimal('0.0000001'), rounding=ROUND_HALF_UP)

print(ans)