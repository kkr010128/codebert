#!/usr/bin/env python3
import sys
import math

a, b = map(int, input().split())

c = math.ceil(b / 0.1)

for i in range(c, c + 10):
    if math.floor(i * 0.1) == b:
        if math.floor(i * 0.08) == a:
            print(i)
            sys.exit()

print(-1)