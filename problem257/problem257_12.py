#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


N = int(input())
A = list(map(int, input().split()))

count = 0
pos = 1
for i, a in enumerate(A):
    if a == pos:
        pos += 1
    else:
        count += 1

if count <= N - 1:
    print(count)
else:
    print(-1)

