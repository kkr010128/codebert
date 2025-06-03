# ALDS1_3_B
# coding: utf-8

from collections import deque

n, q = [int(i) for i in raw_input().split()]
d = deque()
for i in range(n):
    name, time = raw_input().split()
    time = int(time)
    d.append([name, time])

total = 0
while len(d) > 0:
    p = d.popleft()
    if p[1] <= q: # 終わり
        total += p[1]
        print "{} {}".format(p[0], total)
    else:
        total += q
        p[1] -= q
        d.append(p)
