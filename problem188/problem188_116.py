import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

X, Y, A, B, C = map(int, readline().split())
p = list(map(int, readline().split()))
q = list(map(int, readline().split()))
r = list(map(int, readline().split()))

p = sorted(p, reverse=True)[:X]
q = sorted(q, reverse=True)[:Y]

bag = p + q + r
bag = sorted(bag, reverse=True)
print(sum(bag[:(X + Y)]))
