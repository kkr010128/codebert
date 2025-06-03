#!/usr/bin/env python

import math

if __name__ == '__main__':
    a, b, C = map(float, raw_input().split())
    S = a * b * math.sin(C*math.pi/180) / 2
    L = a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C*math.pi/180))
    h = b * math.sin(C*math.pi/180)

    print '{}\n{}\n{}'.format(S, L, h)

