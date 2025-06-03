from decimal import Decimal

A, B = input().split()

A = int(A)
if len(B) == 1:
    B = int(B[0] + '00')
elif len(B) == 3:
    B = int(B[0] + B[2] + '0')
else:
    B = int(B[0]+B[2]+B[3])

x = str(A*B)

print(x[:-2] if len(x) > 2 else 0)
