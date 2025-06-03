#!/usr/bin/env python3
_, *a = map(int, open(0).read().split())
a.sort()
p = [0] * a[-1]
for i in a:
    for j in range(1, a[-1] // i + 1):
        p[j * i - 1] += j
print(sum(i == 1 for i in p))
