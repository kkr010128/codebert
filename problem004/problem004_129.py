#!/usr/bin/python
import sys

t = raw_input()
for i in range(int(t)):
    x = [int(s) for s in raw_input().split()]
    x.sort()
    if x[0] ** 2 + x[1] ** 2 == x[2] ** 2:
        print "YES"
    else:
        print "NO"