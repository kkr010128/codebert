from decimal import Decimal

A, B = input().split()
A = Decimal(A)
B = Decimal(B)
ans = int(A * B)
print(ans)
