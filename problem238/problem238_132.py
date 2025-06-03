#!/usr/bin/env python3
n, k, s = map(int, input().split())
ans = [0] * n
for i in range(n):
    a = s
    if i >= k:
        a = s + 1 if s + 1 < 10 ** 9 else s - 1
    ans[i] = a
print(*ans, sep=" ")
