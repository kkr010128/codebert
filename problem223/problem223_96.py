#!/usr/bin/env python3
n, k, *P = map(int, open(0).read().split())
p = [(i + 1) / 2 for i in P]
s = [float()]
for i in range(n):
    s.append(s[i] + p[i])
print(max(s[i + k] - s[i] for i in range(n - k + 1)))
