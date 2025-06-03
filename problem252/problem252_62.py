#!/usr/bin/env python3
import sys
input = sys.stdin.readline
import bisect

n, m = map(int, input().split())
a = [int(item) for item in input().split()]
a.sort()
a_rev = sorted(a, reverse=True)

cumsum = [0]
for item in a:
    cumsum.append(cumsum[-1] + item)

# Use pair which sum goes over mid
l = 0; r = 10**10
while r - l > 1:
    mid = (l + r) // 2
    to_use = 0
    for i, item in enumerate(a_rev):
        useless = bisect.bisect_left(a, mid - item)
        to_use += n - useless
    if to_use >= m:
        l = mid
    else:
        r = mid
ans = 0
total_use = 0
for i, item in enumerate(a_rev):
    useless = bisect.bisect_left(a, l - item)
    to_use = n - useless
    total_use += to_use
    ans += item * to_use + cumsum[n] - cumsum[n - to_use]
print(ans - l * (total_use - m))