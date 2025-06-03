#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
b = [0] * 60
ans = 0
for i in range(n):
    for j in range(60):
        ans += (i - b[j] if a[i] >> j & 1 else b[j]) << j
    ans %= 10**9 + 7
    for j in range(60):
        b[j] += a[i] >> j & 1
print(ans)
