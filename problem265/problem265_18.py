n = int(input())

from decimal import Decimal

def calc(n):
    for i in range(60000):
        if int(Decimal(i) * Decimal('1.08')) == n:
            return i
    return ':('

print(calc(n))