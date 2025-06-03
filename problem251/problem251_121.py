#!/usr/bin/env python3
n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = [i for i in input()]
b = [0] * n
for i in range(n - k):
    if t[i] == t[i + k] and b[i] == 0:
        if t[i] == 's':
            b[i + k] -= r
        elif t[i] == 'p':
            b[i + k] -= s
        else:
            b[i + k] -= p
print(t.count('s') * r + t.count('p') * s + t.count('r') * p + sum(b))
