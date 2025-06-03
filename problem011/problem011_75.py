import sys
import math

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)

x, y = map(int, raw_input().split())
print gcd(min(x, y), max(x, y))