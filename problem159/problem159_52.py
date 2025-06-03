from decimal import (Decimal, ROUND_DOWN)
x=Decimal(input())
year = 0
money = 100

while money < x:
  money += Decimal(money / 100).quantize(Decimal('0'), rounding=ROUND_DOWN)
  year += 1
print(year)
