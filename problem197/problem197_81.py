from decimal import Decimal
 
a, b, c = [Decimal(x) for x in input().split()]
 
result = a.sqrt() + b.sqrt() < c.sqrt()
print('Yes' if result else 'No')