#!/usr/bin/env python3
n, r = map(int, input().split())
print(r + 100 * (10 - n) * (10 > n))
