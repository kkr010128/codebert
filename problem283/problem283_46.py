#!/usr/bin/env python3
n = int(input())
ans = 0
for i in range(1, n // 2 + 1):
    if i == n - i: break
    ans += 1
print(ans)
