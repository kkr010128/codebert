#!/usr/bin/env python3
s = input()
k = int(input())
n = len(s)
b = [0] * n
c = [0] * n
c[0] = 1

for i in range(n):
    if s[i - 1] == s[i] and not c[i - 1]:
        c[i] = 1
    if i and s[i - 1] == s[i] and not b[i - 1]:
        b[i] = 1
s1 = sum(b)
s2 = sum(c)
if s[-1] != s[0] or b[-1]:
    print(s1 * k)
else:
    if c[-1]:
        print((s1 + s2) * (k // 2) + s1 * (k % 2))
    else:
        print(s1 + (k - 1) * s2)
