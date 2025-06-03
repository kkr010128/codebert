#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
b = [0] * 60
c = [0] * 60
ans = 0
for i in range(n):
    for j in range(60):
        c[j] += i - b[j] if a[i] >> j & 1 else b[j]
        b[j] += a[i] >> j & 1
for j in range(60):
    ans += c[j] << j
print(ans % (10**9 + 7))
