# C - Sqrt Inequality
import decimal
a,b,c = input().split()
a,b,c = map(decimal.Decimal,[a,b,c])
sqrt = decimal.Decimal(0.5)
if a**sqrt + b**sqrt < c**sqrt:
    print('Yes')
else:
    print('No')