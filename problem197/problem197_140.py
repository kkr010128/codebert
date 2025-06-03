import decimal
import math
a, b, c = map(decimal.Decimal, input().split())
if 4 * a * b < (c-a-b) ** 2 and 0 < c-a-b:
  print("Yes")
else:
  print("No")