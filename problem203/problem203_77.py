#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
a, b = [int(x) for x in input().split()]
try:
    print(next(x for x in range(2000) if 8 * x // 100 == a and 10 * x // 100 == b))
except StopIteration:
    print(-1)