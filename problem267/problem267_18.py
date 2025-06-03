#!/usr/bin/env python3
n = int(input())
s = input()
s = [int(i) for i in s]
c = 0
for i in range(10):
    for j in range(10):
        if i in s:
            t = s[s.index(i) + 1:]
            if j in t:
                c += len(set(t[t.index(j) + 1:]))
print(c)
