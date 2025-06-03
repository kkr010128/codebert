# -*- coding: utf-8 -*-
n = input()
x = y = 0
for _ in xrange(n):
 a, b = raw_input().split()
 if a==b:
  x += 1
  y += 1
 elif a>b:
  x += 3
 else:
  y += 3
print x, y