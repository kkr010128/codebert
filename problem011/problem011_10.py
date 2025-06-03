#!/usr/bin/env python
# coding: utf-8

def gcd ( ax, ay):
    x = ax
    y = ay
    while (True):
        if x < y :
            tmp = x
            x = y
            y = tmp
        x=x %y
        if x == 0:
            return y
        elif x == 1:
            return 1



x,y = map(int, input().split())
print(gcd(x,y))
