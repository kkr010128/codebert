#!/usr/bin/env python3
a, b, c = map(int, input().split())
k = int(input())
for _ in range(k):
    if a >= b:
        b *= 2
    elif b >= c:
        c *= 2
print(["No", "Yes"][a < b < c])
