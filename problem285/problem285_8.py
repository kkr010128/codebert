#!/usr/bin/env python3

s = input()
n = len(s)+1
a = [0 for _  in range(n)]

for i in range(n-1):
    if s[i] == '<':
        a[i+1] = max(a[i+1], a[i]+1)

for i in reversed(range(1, n)):
    if s[i-1] == '>':
        a[i-1] = max(a[i-1], a[i]+1)

ans = sum(a)

#print('a = ', a)
print(ans)
