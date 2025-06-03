#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
C = input()

left = 0
right = N-1
count = 0

while left < right:
    if C[left] == 'W' and C[right] == 'R':
        count += 1
        left += 1
        right -= 1

    if C[left] == 'R':
        left += 1
    if C[right] == 'W':
        right -= 1

print(count)
