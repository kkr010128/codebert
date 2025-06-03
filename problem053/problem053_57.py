#!/usr/bin/python

n = input()
a = input().split()
a.reverse()

for (i, item) in enumerate(a):
  print(str(item), end = ' ' if i != len(a)-1 else '\n')