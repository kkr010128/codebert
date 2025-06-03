# -*- coding:utf-8 -*-

import sys

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

array = []
for i in sys.stdin:
    array.append(i)

for i in range(len(array)):
    n, m = array[i].split()
    n, m = int(n), int(m)
    print(int(gcd(n, m)),int(lcm(n, m)))