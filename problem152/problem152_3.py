import sys
import itertools
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
# n = map(int, readline().split())
n = int(readline())

ls = []
rs = []

total = 0
S = list(map(lambda x: x.strip().decode(), readlines()))

for i in range(n):
    s = S[i]

    b = 0
    h = 0
    for c in s:
        if c == '(':
            h += 1
        else:
            h -= 1
            b = min(b, h)

    if h >= 0:
        ls.append((b, h))
    else:
        rs.append((b - h, -h))
    total += h

if total != 0:
    print("No")
    exit()

ls = sorted(ls, reverse=True)
rs = sorted(rs, reverse=True)

h = 0
OK = True
for p in ls:
    b = h + p[0]
    h += p[1]
    if b < 0:
        OK = False

h = 0
for p in rs:
    b = h + p[0]
    h += p[1]
    if b < 0 or h < 0:
        OK = False

if not OK:
    print("No")
else:
    print("Yes")


