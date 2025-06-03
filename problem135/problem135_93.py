import math
from decimal import Decimal
A, B = input().split()
A = int(A)
B = Decimal(B)
C = A * B
ans = math.floor(C)
print(ans)
