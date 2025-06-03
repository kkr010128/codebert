import math
from decimal import Decimal
A, B = list(map(str, input().split()))
print(math.floor(Decimal(A) * Decimal(B)))