#!/usr/bin/env python3
(n, ), *r = [[*map(int, i.split())] for i in open(0)]
s = sorted([[x + l, x - l] for x, l in r])
c = 1
p = s[0][0]
for i in s[1:]:
    if i[1] >= p:
        c += 1
        p = i[0]
print(c)
