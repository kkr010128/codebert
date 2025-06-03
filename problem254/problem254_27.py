#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

A = int(input())
B = int(input())

for i in range(1, 4):
    if i not in (A, B):
        print(i)


