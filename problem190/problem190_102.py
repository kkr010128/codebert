#!/usr/bin/env python3
s = input()
n = len(s)
t = s[:(n - 1) // 2]
u = s[(n + 1) // 2:]
print("YNeos"[any([s != s[::-1], t != t[::-1], u != u[::-1]])::2])
