import sys
import heapq
from decimal import Decimal

input = sys.stdin.readline
a, b, c = map(str, input().split())

root_a = Decimal(a)**Decimal('0.5')
root_b = Decimal(b)**Decimal('0.5')
root_c = Decimal(c)**Decimal('0.5')


if root_a + root_b < root_c:
    print("Yes")
else:
    print("No")