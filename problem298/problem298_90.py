# -*- coding: utf-8 -*-

n, k = map(int, input().split())
cnt = 0

h = list(map(int, input().split()))

for high in h:
    if high >= k:
        cnt += 1


print(cnt)
