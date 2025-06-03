#!/usr/bin/env python3

l, r, d = map(int, input().split())
n = (l-1) // d + 1
m = r // d
print(m-n+1)