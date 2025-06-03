#coding: utf-8

import sys

def gojo(a,b):
    if b % a == 0:
        return a
    else:
        return gojo(b % a, a)

for line in sys.stdin:
    l = map(int,line.split())
    l.sort()
    a = l[0]
    b = l[1]
    print gojo(a,b),a*b/gojo(a,b)