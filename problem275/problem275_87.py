#!/usr/bin/env python3
x, y = map(int, input().split())
ans = (x == y == 1) * 400000
ans += 100000 * max(0, 4 - x)
ans += 100000 * max(0, 4 - y)
print(ans)
