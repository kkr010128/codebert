#!/usr/bin/python
import sys

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a,b):
    return a / gcd(a,b) * b

for l in sys.stdin:
    a = [int(s) for s in l.split()]
    print str(gcd(a[0],a[1]))+" "+str(lcm(a[0],a[1]))