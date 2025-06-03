#!/usr/bin/env python3
a, b = map(int, input().split())
print(a * b * (a < 10 and b < 10) or -1)
