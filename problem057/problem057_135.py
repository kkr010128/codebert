#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
??´?????????
"""

while True:
    inp = input().strip().split(" ")
    m = int(inp[0])
    f = int(inp[1])
    r = int(inp[2])
#    print(inp[1])
    
    if m < 0 and f < 0 and r < 0 :
        break
    
    if m < 0 or f < 0 :
        S = "F"
    else:
        t = m + f
        if t < 30:
            S = "F"
        elif t < 50:
            if r >= 50:
                S = "C"
            else:
                S = "D"
        elif t < 65:
            S = "C"
        elif t < 80:
            S = "B"
        else:
            S = "A"

    print(S)