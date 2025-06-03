# -*- coding: utf-8 -*-
import sys
import fractions

def lcm(a,b):
    return a / fractions.gcd(a,b) * b

for s in sys.stdin:
    a,b = map(int,s.split())
    gcd_ab = fractions.gcd(a,b)
    lcm_ab = lcm(a,b)

    print gcd_ab,lcm_ab