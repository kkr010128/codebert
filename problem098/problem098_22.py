import sys
import numpy as np  # noqa

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


K = int(readline())
C = readline().rstrip().decode()

a = 0  # a: 赤から白に変える操作
b = 0  # b: 白から赤に変える操作
for i in range(len(C)):
    if C[i] == 'R':
        a += 1
mn = a
for i in range(len(C)):
    if C[i] == 'R':
        a -= 1
    else:
        b += 1
    mn = min(mn, min(a, b) + abs(a-b))
print(mn)
