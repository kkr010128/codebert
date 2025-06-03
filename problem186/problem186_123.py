#!/usr/bin/env python3
k, n = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
maxku = 0
for i in range(n-1):
     ku = a[i + 1] - a[i]
     maxku = max(ku, maxku)
     cnt += ku

ku = a[0] + (k - a[-1])
maxku = max(ku, maxku)
cnt += ku

print(cnt - maxku)
