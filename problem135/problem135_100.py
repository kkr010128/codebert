from decimal import Decimal
import math

AB = input().split()
A, B = int(AB[0]), Decimal(AB[1])


print(math.floor(A*B))
