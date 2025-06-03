#!/usr/bin/env python3
s = input()
a = 0
for i in range(len(s)//2):
    a += s[i] != s[-i-1]
print(a)