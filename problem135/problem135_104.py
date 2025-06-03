import sys
import math
def input(): return sys.stdin.readline().rstrip()
from decimal import Decimal

A,B = input().split()
A = int(A)
B = Decimal(B)

print(int(math.floor(A * B)))