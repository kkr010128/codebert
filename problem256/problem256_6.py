#!/usr/bin/env python3

import sys
from math import gcd
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


A, B = map(int, input().split())

gc = gcd(A, B)
LCM = A * B // gc

print(LCM)

