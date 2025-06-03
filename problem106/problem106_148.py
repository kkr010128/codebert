#!/usr/bin/env python3
n = int(input())
ans = [0] * (n + 1)
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            w = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if w <= n:
                ans[w] += 1
for i in range(1, n + 1):
    print(ans[i])
