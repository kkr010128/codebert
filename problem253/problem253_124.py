#!/usr/bin/env python3
n, a, b = map(int, input().split())
if (b - a) % 2 < 1:
    print((b - a) // 2)
else:
    print(min((a + b - 1) // 2, (2 * n - a - b + 1) // 2))
