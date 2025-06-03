#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
L = int(input())
print(f'{(L / 3) ** 3:.6f}')