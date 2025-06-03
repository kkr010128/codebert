#!/usr/bin/env python3

x, y = [int(x) for x in input().split()]
p = [300000, 200000, 100000]
if x == 1 and y == 1:
    print(1000000)
elif x <= 3 and y <= 3:
    print(p[x - 1] + p[y - 1])
elif x <= 3:
    print(p[x - 1])
elif y <= 3:
    print(p[y - 1])
else:
    print(0)
