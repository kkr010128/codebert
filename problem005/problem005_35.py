# -*- coding: utf-8 -*-
import math
errerN=1

while errerN:
    try:
        a=list(map(int, input().split()))
        gcdN=math.gcd(a[0],a[1])
        print(gcdN, int(a[0]*a[1]/gcdN))
    except :
        errerN=0
