# -*- coding: utf-8 -*-

import sys
import os

def gcd(a, b):
    # big - small
    while a != b:
        if a > b:
            a, b = b, a
        a, b = b - a, a
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

lst = sys.stdin.readlines()
for s in lst:
    a, b = map(int, s.split())
    G = gcd(a, b)
    L = lcm(a, b)
    print(G, L)