def input_int():
    return map(int, input().split())

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

import math
from decimal import Decimal

A, B = input().split()

# A=int(A)
# B=float(B)

temp = Decimal(A)*Decimal(B)
print(int(math.floor(temp)))