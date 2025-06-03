#!/usr/bin/env python3
s = input()
c = 0
a = 0
p = ""
n = 0
for i in s:
    if i != p:
        if i == "<":
            if c < 0:
                a -= c * n
            else:
                a -= c * (n - 1)
            n = 2
            c = 1
        else:
            n = 2
            c -= 1
    else:
        if i == "<":
            c += 1
            n += 1
        else:
            c -= 1
            n += 1
    a += c
    p = i
if p == ">":
    if c < 0:
        a -= c * n
    else:
        a -= c * (n - 1)
print(a)
