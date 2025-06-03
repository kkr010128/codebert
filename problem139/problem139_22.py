#! /usr/bin/env python3
import sys
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

H1, M1, H2, M2, K = map(int, read().split())
start = H1 * 60 + M1
end = H2 * 60 + M2

gap = end - start

res = gap - K

print(res)